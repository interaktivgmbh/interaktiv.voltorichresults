# interaktiv.voltorichresults

A Plone 6 backend addon for managing Google Rich Results (structured data / schema.org JSON-LD) in Volto.

This addon provides the backend components required to store and serve Rich Results data for Plone content, working in conjunction with the `@interaktiv/volto-richresults` Volto addon.

## Features

- Dexterity behavior for storing Rich Results data as JSON
- REST API endpoint for fetching Rich Results configuration
- Control panel for site-wide configuration
- Vocabulary for available content types
- Permission-based access control

## Requirements

- Plone 6.0+
- Python 3.11+
- plone.restapi

## Installation

### Using pip

```bash
pip install interaktiv.voltorichresults
```

### Using buildout

Add to your `buildout.cfg`:

```ini
[buildout]
eggs +=
    interaktiv.voltorichresults
```

Then run:

```bash
bin/buildout
```

### Activate the addon

1. Go to Site Setup > Add-ons
2. Install "Interaktiv Volto Rich Results"

## Usage

### Adding the Behavior to Content Types

Add the `IRichResults` behavior to content types that should support Rich Results:

#### Via GenericSetup (recommended)

```xml
<!-- profiles/default/types/Document.xml -->
<?xml version="1.0" encoding="utf-8"?>
<object xmlns:i18n="http://xml.zope.org/namespaces/i18n"
        name="Document"
        meta_type="Dexterity FTI"
        i18n:domain="plone">
  <property name="behaviors" purge="false">
    <element value="interaktiv.voltorichresults.behaviors.richresults.IRichResults"/>
  </property>
</object>
```

#### Via Control Panel

1. Go to Site Setup > Dexterity Content Types
2. Select the content type
3. Go to Behaviors tab
4. Enable "Rich Results"

### Control Panel

Configure which Rich Result types are available for each content type:

1. Go to Site Setup > Rich Results Settings
2. Add content type mappings
3. Select which Rich Result types should be available

### REST API

The addon provides a REST API endpoint for fetching the Rich Results configuration:

```
GET /@richresults-config
```

Response:

```json
{
  "selectable_types": {
    "Document": ["Article", "WebPage"],
    "News Item": ["NewsArticle", "Article"],
    "Event": ["Event"]
  }
}
```

### Permissions

The addon defines two permissions:

| Permission | Description | Default Roles |
|------------|-------------|---------------|
| `InteraktivVoltoRichResults: Configure` | Access Rich Results control panel | Manager, Site Administrator |
| `InteraktivVoltoRichResults: Manage` | Manage Rich Results on content | Manager, Site Administrator, Editor, Owner |

## Development

### Project Structure

```
src/interaktiv/voltorichresults/
├── __init__.py
├── behaviors/
│   ├── __init__.py          # IRichResults behavior
│   └── configure.zcml
├── controlpanels/
│   ├── __init__.py          # Control panel schema
│   └── configure.zcml
├── services/
│   └── richresults_config/
│       ├── __init__.py
│       └── get.py           # REST API endpoint
├── vocabularies/
│   ├── __init__.py          # Content types vocabulary
│   └── configure.zcml
├── profiles/
│   ├── default/             # Installation profile
│   └── uninstall/           # Uninstall profile
├── tests/
│   ├── test_setup.py
│   ├── test_controlpanels.py
│   └── test_rolemap.py
└── configure.zcml
```

### Running Tests

```bash
# Using pytest
pytest

# Or using zope.testrunner
bin/test -s interaktiv.voltorichresults
```

### Test Coverage

```bash
pytest --cov=interaktiv.voltorichresults
```

## License

GPL version 2

## Author

[Interaktiv GmbH](https://www.interaktiv.de)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Related

- [@interaktiv/volto-richresults](https://github.com/interaktivgmbh/volto-richresults) - Frontend addon for Volto
- [Google Rich Results Documentation](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)
- [Schema.org](https://schema.org/)
