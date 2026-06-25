# Create Dictionary
details = {
    "emp_name": "Madhuri",
    "marks": 90,
    "skills": ["Python", "AI", "ML"]
}

# Print dictionary
print("Original Dictionary:")
print(details)

# Access value using key
print("\nEmployee Name:", details["emp_name"])

# Add new key-value pair
details["age"] = 21
print("\nAfter Adding Age:")
print(details)

# Update existing key
details["marks"] = 95
print("\nAfter Updating Marks:")
print(details)

# Get method
print("\nUsing Get Method:")
print(details.get("emp_name"))
print(details.get("emp_id"))  # Returns None

# Keys method
print("\nKeys:")
print(details.keys())

# Values method
print("\nValues:")
print(details.values())

# Items method
print("\nItems:")
print(details.items())

# Pop method
details.pop("age")
print("\nAfter Pop Age:")
print(details)

# Popitem method
details.popitem()
print("\nAfter Popitem:")
print(details)

# Update method
details.update({"city": "Ongole"})
print("\nAfter Update:")
print(details)

# Length of dictionary
print("\nLength:", len(details))

# Clear dictionary
details.clear()
print("\nAfter Clear:")
print(details)