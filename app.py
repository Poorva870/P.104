from collections import Counter 
import csv 
def get_mean(total_weight, total_entries): 
    mean = total_weight / total_entries 
    print(f"Mean (Average) is -> {mean:2f}") 
    
def get_median(total_entries, sorted_data): 
    if total_entries % 2 == 0: 
        median1 = float(sorted_data[total_entries//2]) 
        median2 = float(sorted_data[total_entries//2 - 1]) 
        median = (median1 + median2) / 2 
    else: 
        median = float(sorted_data[total_entries//2]) 
        print(f"Median is -> {median:2f}") 
        
def get_mode(sorted_data): 
    data = Counter(sorted_data) 
    mode_data_for_range = { 
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0, 
        "125-135": 0,
        "135-145": 0, 
        "145-155": 0, 
        "155-165": 0, 
        "165-175": 0 
        } 
    for weight, occurence in data.items():
         if 75 < weight < 85:
             mode_data_for_range["75-85"] += occurence 
         elif 85 < weight < 95: 
             mode_data_for_range["85-95"] += occurence 
         elif 95 < weight < 105: 
             mode_data_for_range["95-105"] += occurence 
         elif 105 < weight < 115: 
             mode_data_for_range["105-115"] += occurence 
         elif 115 < weight < 125:
             mode_data_for_range["115-125"] += occurence 
         elif 125 < weight < 135: 
             mode_data_for_range["125-135"] += occurence 
         elif 135 < weight < 145: 
             mode_data_for_range["135-145"] += occurence 
         elif 145 < weight < 155: 
             mode_data_for_range["145-155"] += occurence 
         elif 155 < weight < 165: 
             mode_data_for_range["155-165"] += occurence 
         elif 165 < weight < 175: 
             mode_data_for_range["165-175"] += occure