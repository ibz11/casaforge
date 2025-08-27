import frappe
from.utils import api_response



@frappe.whitelist()
def fetch_featured_facilities():
    pass


@frappe.whitelist()
def fetch_all_properties():
    properties=frappe.get_list('Property Listing',fields="*")
    results = []
    for prop in properties:
        doc = frappe.get_doc("Property Listing", prop.name)

        # fetch child table images
        images = []
        for img in doc.property_images:   # assuming child table fieldname is 'property_images'
            # images.append({
            #     "image": img.attach_image  # child field Attach Image
            # })
            images.append(img.attach_image )

        # attach to response
        prop["images"] = images
        results.append(prop)
    return api_response(success=True,data=results,message="Properties retrieved succesfully " , status_code=200)
    

@frappe.whitelist()
def fetch_single_property(**kwargs):
    """
    title
    description
    property_details: 5 Bedrooms , 4 Bathrooms , 4,500 Sq Ft 
    year_built:2020
    images: 4-10
      property_type: House , Condo , Townhouse , Apartment , Commercial
    lot_size: 1.2 acres
    price:
    location:
    listed_date: {created at} or timestamp
    Property ID: #
    featured:true or false
    hide:true or false
    ---------------------
    Contact Agent Fields
    ---------------------
    full_names:Sarah Johnson
    title:Licensed Real Estate Agent
    phone_number:(555) 123-4567
    email:sarah@luxuryrealty.com
    """
    
   
    pass


@frappe.whitelist()
def filter_search_property(**kwargs):
    """
    Price Range:  $0 - $5.0M
    Location:Enter city , address or Zip
    Bedrooms: 1-5+
    Bathrooms: 1-4+
    square_footage:  0 - 10,000 sqft
    property_type: House , Condo , Townhouse , Apartment , Commercial
    """
    pass

