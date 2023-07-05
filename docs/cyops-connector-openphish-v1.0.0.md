## About the connector
OpenPhish helps to automatically identify zero-day phishing sites and provide comprehensive, actionable, real-time threat intelligence by using proprietary Artificial Intelligence algorithms.
<p>This document provides information about the OpenPhish Connector, which facilitates automated interactions, with a OpenPhish server using FortiSOAR&trade; playbooks. Add the OpenPhish Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with OpenPhish.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-openphish`

## Prerequisites to configuring the connector
- You must have the URL of OpenPhish server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the OpenPhish server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>OpenPhish</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Server url to get feeds data.<br>
<tr><td>Access Key<br></td><td>Required access Key for openphish service authentication.<br>
<tr><td>Secret Access Key<br></td><td>Required secret access key for openphish service authentication.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Indicators For Latest Feed <br></td><td>Retrieves a list of all indicators from openphish feed for last 15 minutes.<br></td><td>get_indicators_for_latest_feed <br/>Investigation<br></td></tr>
<tr><td>Get Indicators For 24 Hr Feed <br></td><td>Retrieves a list of all indicators from openphish Feed for last 24 hours.<br></td><td>get_indicators_for_24h_feed <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Indicators For Latest Feed 
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sector": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "brand": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "isotime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asn_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "discover_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "family_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "host": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "country_code": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "tld": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "country_name": ""
</code><code><br>}</code>

### operation: Get Indicators For 24 Hr Feed 
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sector": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ip": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "brand": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "isotime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asn_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "discover_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "family_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "host": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "country_code": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "tld": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "country_name": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - openphish - 1.0.0` playbook collection comes bundled with the OpenPhish connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the OpenPhish connector.

- Get Indicators For 24 Hr Feed 
- Get Indicators For Latest Feed 

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
