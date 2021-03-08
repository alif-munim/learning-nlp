import json

training_data = [
    {
        "labels": ["Meetings"],
        "key_phrases": ["meetings", "meet", "talk", "discuss", "zoom", "skype", "webex"]
    },
    {
        "labels": ["Meetings", "Initiate"],
        "key_phrases": ["schedule", "book a time"]
    },
    {
        "labels": ["Meetings", "Amend", "Reschedule"],
        "key_phrases": ["reschedule", "better time"]
    },
    {
        "labels": ["Meetings", "Amend", "Cancel"],
        "key_phrases": ["cancel", "unavailable"]
    },
    {
        "labels": ["Contacts"],
        "key_phrases": ["contacts", "contact information"]
    },
    {
        "labels": ["Contacts", "Individual"],
        "key_phrases": ["project lead", "manager", "supervisor", "squad leader", "owner"]
    },
    {
        "labels": ["Contacts", "List"],
        "key_phrases": ["list", "spreadsheet", "csv", "data set"]
    },
    {
        "labels": ["Contacts", "List", "Mailing List"],
        "key_phrases": ["mailing list", "marketing", "engagement", "increase engagement", "generate interest", "promote"]
    },
    {
        "labels": ["Contacts", "List", "Leads"],
        "key_phrases": ["leads", "potential buyers", "interested parties", "purchases"]
    },
]

training_data_filename = "training_data.json"
with open(training_data_filename, 'w', encoding='utf-8') as f:
    json.dump(training_data, f)
