subject = ["maths","physics","chemistery"]
marks= [85,94,92]

report_card = dict(zip(subject,marks))

higest = max(report_card,key=report_card.get)

print(f"subject with higest marks is : {higest}")