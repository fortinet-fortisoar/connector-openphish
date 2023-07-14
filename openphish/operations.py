""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
import requests
from .utils import get_headers
from connectors.core.connector import get_logger, ConnectorError
logger = get_logger('open-phish')


class OpenPhish(object):

    def __init__(self, config):
        self.server_url = config.get('server').strip()
        self.aws_access_key = config.get('access_key')
        self.aws_secret_access_key = config.get('secret_access_key')
        self.headers = get_headers(self.server_url, self.aws_access_key, self.aws_secret_access_key, feed_path="/premium/feed.json")
        if not self.server_url.startswith('https://'):
            self.server_url = 'https://{0}/'.format(self.server_url)

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False):
        url = self.server_url + endpoint
        logger.debug('Final url to make rest call is: {0}'.format(url))
        if headers:
            self.headers.update(headers)
        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, self.headers))
            response = requests.request(method, url, headers=self.headers)
            if response.status_code in [200]:
                if health_check:
                    return response
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))


def get_indicators_for_latest_feed(config, params):
    """
    Retrieves a list of all indicators from openphish feed for last 15 minutes.
    :param config: config
    :param params: params
    :return: List of all latest indicators from openphish Feed.
    """
    obj = OpenPhish(config)
    endpoint = '/premium/feed.json'
    return obj.make_api_call(endpoint=endpoint)


def get_indicators_for_24h_feed(config, params):
    """
    Retrieves a list of all indicators from openphish Feed for last 24 hours.
    :param config: config
    :param params: params
    :return: List of all indicators from openphish. Generated feed every 5 minutes entries from last 24 hours you have specified.
    """
    obj = OpenPhish(config)
    endpoint = "/premium/feed_24h.json"
    server_url = config.get('server').strip()
    aws_access_key = config.get('access_key')
    aws_secret_access_key = config.get('secret_access_key')
    headers = get_headers(server_url, aws_access_key, aws_secret_access_key, feed_path=endpoint)
    return obj.make_api_call(endpoint=endpoint, headers=headers)


def _check_health(config):
    try:
        obj = OpenPhish(config)
        obj.make_api_call(endpoint='/premium/feed.json', health_check=True)
        return True
    except Exception as err:
        logger.exception('Health check failed with: {0}'.format(err))
        raise ConnectorError('Health check failed with: {0}'.format(err))


operations = {
    'get_indicators_for_latest_feed': get_indicators_for_latest_feed,
    'get_indicators_for_24h_feed': get_indicators_for_24h_feed
}
