"""
Dummy Dataset Generation Script - Personal Expense Dataset

This module generates a dummy personal expense dataset using the Python's Faker package.
This module serves as a utility tool to develop real-world like datasets for various purposes.
"""

import copy
import uuid
import random
import datetime
import faker
import pandas as pd


def get_customer_data():
    """Utility Function to generate the details of a customer."""
    faker_obj = faker.Faker()
    states = {
        "Andhra Pradesh": "Southern Region",
        "Arunachal Pradesh": "Northeastern Region",
        "Assam": "Northeastern Region",
        "Bihar": "Eastern Region",
        "Chhattisgarh": "Central Region",
        "Goa": "Western Region",
        "Gujarat": "Western Region",
        "Haryana": "Northern Region",
        "Himachal Pradesh": "Northern Region",
        "Jharkhand": "Eastern Region",
        "Karnataka": "Southern Region",
        "Kerala": "Southern Region",
        "Madhya Pradesh": "Central Region",
        "Maharashtra": "Western Region",
        "Manipur": "Northeastern Region",
        "Meghalaya": "Northeastern Region",
        "Mizoram": "Northeastern Region",
        "Nagaland": "Northeastern Region",
        "Odisha": "Eastern Region",
        "Punjab": "Northern Region",
        "Rajasthan": "Northern Region",
        "Sikkim": "Northeastern Region",
        "Tamil Nadu": "Southern Region",
        "Telangana": "Southern Region",
        "Tripura": "Northeastern Region",
        "Uttar Pradesh": "Northern Region",
        "Uttarakhand": "Northern Region",
        "West Bengal": "Eastern Region",
    }
    uid = f"ACC-{uuid.uuid4().hex[:5]}"
    dob = faker_obj.date_of_birth(minimum_age=18, maximum_age=60)
    date_of_birth = dob.strftime("%d-%m-%Y")
    age = (datetime.datetime.today().date() - dob).days // 365
    gender = random.choice(["Male", "Female", "Other"])
    if gender == "Male":
        f_name = faker_obj.first_name_male()
        l_name = faker_obj.last_name_male()
    elif gender == "Female":
        f_name = faker_obj.first_name_female()
        l_name = faker_obj.last_name_female()
    else:
        f_name = faker_obj.first_name_nonbinary()
        l_name = faker_obj.last_name_nonbinary()
    state = random.choice(list(states.keys()))
    region = states.get(state)
    return {
        "uid": uid,
        "name": f"{f_name} {l_name}",
        "dob": date_of_birth,
        "age": age,
        "gender": gender,
        "state": state,
        "region": region,
        "country": "India",
    }


def get_variations():
    """Utility Function to generate the personal daily expense details of a customer."""
    return {
        "Category": random.choice(
            [
                "Groceries",
                "Utilities",
                "Rent/Mortgage",
                "Transportation",
                "Dining Out",
                "Entertainment",
                "Health & Fitness",
                "Clothing",
                "Travel",
                "Insurance",
                "Education",
                "Miscellaneous",
            ]
        ),
        "Payment Method": random.choice(
            [
                "Cash",
                "Credit Card",
                "Debit Card",
                "Online Transfer",
                "Digital Wallet",
                "UPI",
                "Bank Transfer",
                "Check",
            ]
        ),
        "Location": random.choice(
            [
                "Home",
                "Office",
                "Grocery Store",
                "Restaurant",
                "Gas Station",
                "Shopping Mall",
                "Pharmacy",
                "Gym",
                "Travel Destination",
            ]
        ),
        "Expense": round(random.uniform(0, 5000), 2),
    }


def main(customers=1000, start_date="01-01-2022", end_date="01-01-2024"):
    """Main Driver Function to generate the personal expense dataset"""
    date_range = pd.date_range(start_date, end_date)
    print("Generating the Personal Expense Dataset.\nCustomer:", end=" ")
    output_list = []
    for i in range(customers):
        print(i + 1, end=" ")
        output_dict = get_customer_data()
        for date in date_range:
            var_dict = copy.deepcopy(output_dict)
            var_dict["datadate"] = date.strftime("%d-%m-%Y")
            var_dict.update(get_variations())
            output_list.append(var_dict)
    output_df = pd.DataFrame(output_list)
    print("\nDataset Generated Successfully")
    return output_df


if __name__ == "__main__":
    dataset = main()
    dataset.to_csv("personal_expense_dataset.csv", index=False)
