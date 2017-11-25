class Organization(object):
    """An organization.

    Attributes:
        name: A string representing the organization's name
        ubi: The DOR-issued Unified Business Identifier
        address_line_1: Organization physical address (first line)
        address_line_2: Organization physical address (second line)
        city: Organization city
        state: Organization state
        zipcode: Organization zipcode
        county: Organization county
        phone: Organization phone
        license_id: The WSLCB-issued license identifier
        license_type: The license type
        license_status: The license status
        license_creation_date: The license creation/issue date
    """

    def __init__(self, **kwargs):
        """Instantiate an Organization from given keyword arguments."""
        default_values = {
            'name': 'Organization Name',
            'ubi': 'Unified Business Identifier',
            'address_line_1': '',
            'address_line_2': '',
            'city': '',
            'state': '',
            'zipcode': '',
            'county': '',
            'phone': '',
            'license_id': '',
            'license_status': '',
            'license_creation_date': ''
        }

        # Set instance properties from keyword arguments or default values
        for (key, default) in default_values.items():
            setattr(self, key, kwargs.get(key, default))

    @classmethod
    def from_licensed_business(cls, licensed_business):
        """Instantiate an Organization from a WSLCB licensed business."""
        organization = cls()
        organization.name = licensed_business['organization']
        organization.ubi = licensed_business['ubi']
        organization.address_line_1 = licensed_business['address']
        organization.address_line_2 = licensed_business['address_line_2']
        organization.city = licensed_business['city']
        organization.state = licensed_business['state']
        organization.zipcode = licensed_business['zip']
        organization.county = licensed_business['county']
        organization.phone = licensed_business['dayphone']
        organization.license_id = licensed_business['license']
        organization.license_type = licensed_business['type']
        organization.license_status = licensed_business['active']
        organization.license_creation_date = licensed_business['createdate']
        return organization

    def __str__(self):
        """Return a string representation of the Organization."""
        output = '{} ({})\n'.format(self.name, self.ubi)
        output += 'Address: {}\n'.format(self.get_address_string())
        if self.county:
            output += 'County: {}\n'.format(self.county)
        if self.phone:
            output += 'Phone: {}\n'.format(self.phone)
        output += 'License: {}\n'.format(self.get_license_string())
        return output

    def get_address_string(self):
        """Return a string representation of the Organization address."""
        output = ''
        if self.address_line_1:
            output += '{}'.format(self.address_line_1)
        if self.address_line_2:
            output += ', {}'.format(self.address_line_2)
        if self.city:
            output += ', {}'.format(self.city)
        if self.state:
            output += ', {}'.format(self.state)
        if self.zipcode:
            output += '  {}'.format(self.zipcode)
        return output

    def get_license_string(self):
        """Return a string representation of the Organization license."""
        output = ''
        if self.license_id:
            output += '{}'.format(self.license_id)
        if self.license_creation_date:
            output += ' (Created {})'.format(self.license_creation_date)
        if self.license_type:
            output += '\n{}'.format(self.license_type)
        if self.license_status:
            output += ' ({})'.format(self.license_status)
        return output
