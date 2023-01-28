from __init__ import db, Group, Bill

db.create_all()

group1 = Group("Trip to Wonderland")
group2 = Group("Trip to Latvia")
group3 = Group("Trip to Estija")
group4 = Group("Trip to Space")
group5 = Group("Trip to Mountains")
group6 = Group("Trip to USA")
group7 = Group("Trip to Waterfall")
group8 = Group("Trip to Island")
group9 = Group("Trip to Nowhere")
group10 = Group("Trip to Disneyland")

db.session.add_all([group1, group2, group3, group4, group5,
                   group6, group7, group8, group9, group10])
db.session.commit()

bill1 = Bill(group1.id, "10", "Bilietas")
bill2 = Bill(group5.id, "150", "Skrydis")
bill3 = Bill(group1.id, "2", "Ledai")

db.session.add_all([bill1, bill2, bill3])
db.session.commit()
