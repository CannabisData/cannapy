class Organization(object):
    """An organization.

    Attributes:
        name: A string representing the organization's name.
        ubi: The DOR-issued Unified Business Identifier
        address_line_one: Organization physical address (first line)
        address_line_two: Organization physical address (second line)
        city: Organization city
        state: Organization state
        zipcode: Organization zipcode
        county: Organization county
        phone: Organization phone
        license_id: The WSLCB-issued license identifier
        license_type: The license type
        license_status: The license status
        license_creation_date: Date the license was issued
    """

    def __init__(self, name, ubi, address_line_one, address_line_two, city,
                 state, zipcode, county, phone, license_id, license_type,
                 license_status, license_creation_date):
        """Instantiate an Organization object."""
        self.name = name
        self.ubi = ubi
        self.address_line_one = address_line_one
        self.address_line_two = address_line_two
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.county = county
        self.phone = phone
        self.license_id = license_id
        self.license_type = license_type
        self.license_status = license_status
        self.license_creation_date = license_creation_date
