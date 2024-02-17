from PIL import Image, ImageDraw, ImageFont

# Function to create student ID card
def create_id_card(student_info):
    # Load a base template for the ID card
    id_card = Image.open("id_card_template.jpg")
    draw = ImageDraw.Draw(id_card)

    # Define font and size for text
    font = ImageFont.truetype("arial.ttf", size=25)

    # Render student information on the ID card
    draw.text((100, 100), f"Name: {student_info['name']}", fill="black", font=font)
    draw.text((100, 150), f"ID: {student_info['id']}", fill="black", font=font)
    draw.text((100, 200), f"Department: {student_info['department']}", fill="black", font=font)
    draw.text((100, 250), f"Batch: {student_info['batch']}", fill="black", font=font)

    # Save the ID card
    id_card.save(f"{student_info['id']}_id_card.jpg")

# Example student information
student_info = {
    "name": "John Doe",
    "id": "123456",
    "department": "Computer Science",
    "batch": "2023"
}

# Create the ID card
create_id_card(student_info)
  
