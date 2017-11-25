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
            'license_type': '',
            'license_status': '',
            'license_creation_date': ''
        }

        # Set instance properties from keyword arguments or default values
        for (attr, default) in default_values.items():
            setattr(self, attr, kwargs.get(attr, default))

    @classmethod
    def from_licensed_business(cls, licensed_business):
        """Instantiate an Organization from a WSLCB licensed business."""
        attribute_map = {
            'organization': 'name',
            'ubi': 'ubi',
            'address': 'address_line_1',
            'address_line_2': 'address_line_2',
            'city': 'city',
            'state': 'state',
            'zip': 'zipcode',
            'county': 'county',
            'dayphone': 'phone',
            'license': 'license_id',
            'type': 'license_type',
            'active': 'license_status',
            'createdate': 'license_creation_date'
        }

        # Map organization attributes from the licensed business
        org_attributes = {}
        for (source_attr, target_attr) in attribute_map.items():
            org_attributes[target_attr] = licensed_business[source_attr]

        return cls(**org_attributes)

    def __str__(self):
        """Return a string representation of the Organization."""
        output = '{} (UBI {})\n'.format(self.name, self.ubi)
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
            output += ' {}'.format(self.license_type)
        if self.license_status:
            output += ' - {}'.format(self.license_status)
        return output
