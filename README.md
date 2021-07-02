[![PyTest](https://github.com/grigorescu/broker-to-json/actions/workflows/pytest.yaml/badge.svg)](https://github.com/grigorescu/broker-to-json/actions/workflows/pytest.yaml)

# broker-to-json

A couple of small utilities to convert from Zeek Broker data to JSON. Used by eZeeKonfigurator.

Split into two categories:

 * conversions: These need Broker bindings, as they deal with Broker types.
 * utils: These do not need Broker bindings, and parse string arguments.