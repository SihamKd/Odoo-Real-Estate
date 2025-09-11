# App One - Odoo 17 Real Estate Module

A comprehensive **Odoo 17 module** for real estate management with property management, sales integration, custom UI components, and REST API endpoints.

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-LGPL--3-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

## 🏠 Module Overview

**App One** is a standalone Odoo 17 module that provides complete real estate management functionality:

- ✅ **Standalone Module**: Can be installed in any Odoo 17 instance
- ✅ **Full CRUD Operations**: Complete property lifecycle management
- ✅ **REST API**: JSON endpoints for external integrations  
- ✅ **Custom UI Components**: Modern, responsive interface with custom styling
- ✅ **Multi-language**: French and Arabic translations included

## ✨ Key Features

### Property Management
- ✅ Complete property lifecycle management (Draft → Pending → Sold → Closed)
- ✅ Detailed property records with specs (bedrooms, living area, facades, garage, garden)
- ✅ Automated reference number generation
- ✅ Property archiving and history tracking
- ✅ Price calculation and difference analysis
- ✅ Late property detection with automated alerts

### Owner & Client Management
- ✅ Comprehensive owner profiles with contact information
- ✅ One-to-many property relationships
- ✅ Client management system

### Sales Integration
- ✅ Seamless integration with Odoo Sales module
- ✅ Custom sale order modifications for real estate
- ✅ Accounting integration for property transactions
- ✅ Invoice customization for real estate deals

### Security & Access Control
- ✅ Role-based security (Property Manager, Property User)
- ✅ Record-level security rules
- ✅ Field-level permissions

### API & Integration
- ✅ Full REST API for property management
- ✅ JSON endpoints for external integrations
- ✅ Pagination support for large datasets

### Reporting & Analytics
- ✅ Excel (XLSX) report generation
- ✅ Custom property reports
- ✅ Analytics dashboard capabilities

## 🚀 Technology Stack

- **Framework**: Odoo 17 (Python)
- **Database**: PostgreSQL
- **Frontend**: JavaScript, XML, CSS
- **Architecture**: MVC pattern with Odoo ORM
- **Reporting**: XLSX, PDF generation
- **API**: REST API with JSON responses

## 📁 Module Structure

```
app_one/                     # Real Estate Module
├── __init__.py
├── __manifest__.py          # Module configuration
├── controllers/
│   └── property_api.py      # REST API endpoints
├── data/
│   ├── data.xml            # Initial data
│   └── sequence.xml        # Reference sequences
├── models/                 # All business logic
│   ├── __init__.py
│   ├── property.py         # Main property model
│   ├── owner.py            # Owner management
│   ├── building.py         # Building model
│   ├── tag.py              # Property tags
│   ├── client.py           # Client model
│   ├── property_history.py # State tracking
│   ├── sale_order.py       # Sales integration
│   ├── account_move.py     # Invoice customization
│   └── res_partner.py      # Partner extensions
├── reports/
│   ├── property_report.xml # Report templates
│   └── xlsx_property_report.py # Excel reports
├── security/
│   ├── security.xml        # User groups & rules
│   └── ir.model.access.csv # Access permissions
├── static/src/             # Frontend assets
│   ├── css/
│   │   └── property.css    # Main styles
│   └── components/
│       ├── listView/       # Custom list component
│       └── formView/       # Custom form component
├── tests/
│   └── test_property.py    # Unit tests
├── views/                  # XML views
│   ├── base_menu.xml       # Navigation menus
│   ├── property_view.xml   # Property views
│   └── [other view files]
└── wizard/                 # Workflow wizards
    ├── change_state_wizard.py
    └── change_state_wizard_view.xml
```

## 🛠️ Installation Guide

### Prerequisites
- **Odoo 17** instance (Community or Enterprise)
- **PostgreSQL** database
- **Python 3.8+** with Odoo dependencies

### Quick Installation

1. **Download the module**
   ```bash
   git clone https://github.com/SihamKd/Odoo-Real-Estate.git
   cd Odoo-Real-Estate
   ```

2. **Copy module to Odoo addons**
   ```bash
   # Copy app_one to your Odoo addons directory
   cp -r app_one /path/to/your/odoo/addons/
   ```

3. **Update addons list**
   - Restart your Odoo server
   - Go to Apps menu
   - Click "Update Apps List"

4. **Install the module**
   - Search for "App One" or "Real Estate"
   - Click "Install"

### Alternative: Add to custom addons path

1. **Add to odoo.conf**
   ```ini
   [options]
   addons_path = /path/to/odoo/addons,/path/to/custom/addons,/path/to/app_one
   ```

2. **Restart Odoo and install via Apps menu**

### Command Line Installation
```bash
# Install via command line (replace with your database name)
python odoo-bin -i app_one -d your_database_name
```

## 🧪 Testing

```bash
# Run all tests for the module
python odoo-bin --test-enable -i app_one -d your_database

# Run specific test
python odoo-bin --test-tags :TestProperty.test_method -d your_database

# Run module tests only
python odoo-bin --test-tags /app_one -d your_database
```

## ⚙️ Module Dependencies

The module requires these Odoo standard modules:
- `base` - Core Odoo functionality
- `sale_management` - Sales integration
- `account` - Accounting features
- `mail` - Email and activity tracking
- `contacts` - Partner management

*All dependencies are automatically installed with the module.*

## 🔗 API Usage

### Get Properties
```http
GET /api/properties
Content-Type: application/json
```

### Create Property
```http
POST /api/properties
Content-Type: application/json

{
  "name": "Beautiful House",
  "description": "Luxury property with garden",
  "expected_price": 250000,
  "bedrooms": 3,
  "living_area": 120
}
```

## 📸 Screenshots

### Property List View
![Property List View](screenshots/property-list.png)
*Custom styled property list with advanced filtering and search capabilities*

### Property Form View  
![Property Form View](screenshots/property-form.png)
*Comprehensive property form with validation and custom scrollbars*

### Dashboard Analytics
![Dashboard](screenshots/dashboard.png)
*Real-time analytics and reporting dashboard*

> **Note**: Screenshots will be added to the `screenshots/` folder in the repository.

## 📈 Features Highlights

- **Multi-language Support**: French and Arabic translations
- **Workflow Management**: State change wizards with validation
- **Email Integration**: Activity tracking and notifications
- **Custom Validation**: Business rules and constraints
- **Responsive Design**: Modern UI with custom CSS/JS components

## 👥 Development Team

**Author**: Siham Khaddou  
**Version**: 17.0.0.1.0  
**License**: LGPL-3  

## 🙏 Acknowledgments

Special thanks to **Muhammed Nasser** for guidance and mentorship throughout this project.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 📋 Files

```
app_one/                     # 
├── __init__.py
├── __manifest__.py          # Module configuration
├── controllers/             # ✅ API endpoints (no sensitive data)
├── data/                    # ✅ Sample data only
├── models/                  # ✅ Business logic
├── reports/                 # ✅ Report templates
├── security/                # ✅ Access rules (no passwords)
├── static/                  # ✅ CSS/JS assets
├── tests/                   # ✅ Unit tests
├── views/                   # ✅ UI definitions
└── wizard/                  # ✅ Workflow logic
```

## 🐛 Known Issues

- API endpoints require proper authentication headers
- Large datasets may require pagination optimization

## 🔄 Changelog

### v17.0.0.1.0 (Latest)
- ✅ Initial release
- ✅ Core property management features
- ✅ REST API implementation
- ✅ Custom UI components with scrollbars
- ✅ Multi-language support
- ✅ Excel reporting functionality

## 📋 TODO / Roadmap

- [ ] Add property image gallery
- [ ] Implement property search filters
- [ ] Add map integration for property locations
- [ ] Create mobile-responsive views
- [ ] Add property comparison feature
- [ ] Implement automated property valuation

## 📞 Support

For support and questions, please contact:
- **GitHub**: [SihamKd](https://github.com/SihamKd)
