def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return
    
    # Check if all elements in attendees are dictionaries
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for each attendee
        output_content = template
        
        # Replace placeholders with actual values or "N/A"
        output_content = output_content.replace("{name}", str(attendee.get("name", "N/A")) if attendee.get("name") is not None else "N/A")
        output_content = output_content.replace("{event_title}", str(attendee.get("event_title", "N/A")) if attendee.get("event_title") is not None else "N/A")
        output_content = output_content.replace("{event_date}", str(attendee.get("event_date", "N/A")) if attendee.get("event_date") is not None else "N/A")
        output_content = output_content.replace("{event_location}", str(attendee.get("event_location", "N/A")) if attendee.get("event_location") is not None else "N/A")
        
        # Write to output file
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as file:
            file.write(output_content)
