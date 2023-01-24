from __init__ import db, Group, Bill

group1 = Group("1", "Trip to Wonderland")
group2 = Group("2", "Trip to Latvia")
group3 = Group("3", "Trip to Estija")
group4 = Group("4", "Trip to Space")
group5 = Group("5", "Trip to Mountains")
group6 = Group("6", "Trip to USA")
group7 = Group("12", "Trip to Waterfall")
group8 = Group("20", "Trip to Island")
group9 = Group("129", "Trip to Nowhere")
group10 = Group("1000", "Trip to Disneyland")

# bill1 = Bill("1", "Bilietas", "10")
# bill2 = Bill("2", "Skrydis", "150")

db.create_all()
db.session.add_all([group1, group2, group3, group4, group5,
                   group6, group7, group8, group9, group10])
db.session.commit()
