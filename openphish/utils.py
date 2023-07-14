""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import hashlib
import hmac
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError
logger = get_logger('open-phish')


def sign(key, message):
    return hmac.new(key, message.encode("utf-8"), hashlib.sha256).digest()


def get_signature_key(key, datestamp, region, service):
    k_date = sign(("AWS4" + key).encode("utf-8"), datestamp)
    k_region = sign(k_date, region)
    k_service = sign(k_region, service)
    k_signing = sign(k_service, "aws4_request")
    return k_signing


def extract_host_and_region(url):
    if url.startswith('https://'):
        host = url.replace('https://', '')
    else:
        host = url
    url_parts = host.split('.')
    region = url_parts[1].replace('s3-', '')
    return host, region


def get_headers(server_url, access_key, secret_key, feed_path):
    payload = ""
    date = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    host, region = extract_host_and_region(server_url)
    content_sha256 = hashlib.sha256(payload.encode("utf-8")).hexdigest() if payload else hashlib.sha256(b"").hexdigest()
    canonical_request = f"GET\n{feed_path}\n\nhost:{host}\nx-amz-content-sha256:{content_sha256}\nx-amz-date:{date}\n\nhost;x-amz-content-sha256;x-amz-date\n{content_sha256}"
    string_to_sign = f"AWS4-HMAC-SHA256\n{date}\n{date[:8]}/{region}/s3/aws4_request\n{hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()}"
    signing_key = get_signature_key(secret_key, date[:8], region, "s3")
    signature = hmac.new(signing_key, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()

    headers = {
        "X-Amz-Content-Sha256": content_sha256,
        "X-Amz-Date": date,
        "Authorization": f"AWS4-HMAC-SHA256 Credential={access_key}/{date[:8]}/{region}/s3/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature={signature}"
    }

    return headers

