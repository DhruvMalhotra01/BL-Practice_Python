friends = {
        "Friend1": [
            {"City": "New York", "Pincode": "10001"},
            {"email-id": "john.doe@email.com", "PhoneNumber": "917-555-1234"}
        ],
        "Friend2": [
            {"City": "Los Angeles", "Pincode": "90001"},
            {"email-id": "sarah.wilson@email.com", "PhoneNumber": "310-555-5678"}
        ],
        "Friend3": [
            {"City": "Chicago", "Pincode": "60601"},
            {"email-id": "mike.johnson@email.com", "PhoneNumber": "312-555-9012"}
        ],
        "Friend4": [
            {"City": "Houston", "Pincode": "77001"},
            {"email-id": "emily.davis@email.com", "PhoneNumber": "713-555-3456"}
        ],
        "Friend5": [
            {"City": "Miami", "Pincode": "33101"},
            {"email-id": "chris.martinez@email.com", "PhoneNumber": "305-555-7890"}
        ]
    }
    

def get_details() -> None:
    friend_name = input("Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5):  ")
    detail_type = input("Enter detail type (City/Pincode/Email/PhoneNumber): ")
    
    if friend_name in friends:
        print(friend_name)
        
        if detail_type in friends[friend_name][0] or detail_type in friends[friend_name][1] :
            if detail_type in friends[friend_name][0]:
                print(f"{detail_type} of {friend_name} : {friends[friend_name][0][detail_type ]}")
            
            else:
                print(f"{detail_type} of {friend_name} : {friends[friend_name][1 ][detail_type]}")
        
        else:
            print("Invalid detail serached")
    
    else:
        print("Wrong Friend Name ")

def main():
    
    get_details() 
   

if __name__ == "__main__":
    main()