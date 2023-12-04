print("Please Enter costs for 2022")
personal_cost = int(input("Personal cost "))
Travelling_cost = int(input("Travelling cost "))
software_cost = int(input("Tool/Equipment/Software/Publication Cost "))
service_cost = int(input("Domestic R & D Service Cost "))
Consultancies_cost = int(input("Consultancies and Services Cost: "))
Materials_cost = int(input("Materials Cost: "))
Patent_cost = int(input("Patent Rights Cost: "))
Total_cost = 0
cumulative_cost = 0
year = 2023

for i in range(0,2):
    print("Please Enter costs for " + str(year)+"\n\n\n")
    personal_cost = int(input("Personal cost "))
    Travelling_cost = int(input("Travelling cost "))
    software_cost = int(input("Tool/Equipment/Software/Publication Cost "))
    service_cost = int(input("Domestic R & D Service Cost "))
    Consultancies_cost = int(input("Consultancies and Services Cost: "))
    Materials_cost = int(input("Materials Cost: "))
    Patent_cost = int(input("Patent Rights Cost: "))
    Total_cost = personal_cost+Travelling_cost+software_cost+service_cost+Consultancies_cost+Materials_cost+Patent_cost
    cumulative_cost = Total_cost
    fr_personal_cost = personal_cost/Total_cost*100
    fr_Travelling_cost = Travelling_cost/Total_cost*100
    fr_software_cost = software_cost/Total_cost*100
    fr_service_cost = service_cost/Total_cost*100
    fr_Consultancies_cost = Consultancies_cost/Total_cost*100
    fr_Materials_cost = Materials_cost/Total_cost*100
    fr_Patent_cost = Patent_cost/Total_cost*100
    year += 1
print( "fractional Personal cost: " + str(fr_personal_cost))
print("fractional Travelling_cost: " + str(fr_Travelling_cost))
print("fractional software_cost: "+str(fr_software_cost))
print("fractional service_cost: "+str(fr_service_cost))
print("fractional Consultancies_cost: "+str(fr_Consultancies_cost))
print("fractional Materials_cost: "+str(fr_Materials_cost))
print("fractional Patent_cost: "+str(fr_Patent_cost))
print("Total cost: "+ str(Total_cost))

