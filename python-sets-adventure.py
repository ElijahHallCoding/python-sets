# Task 1: Flight Route Comparison

# Flight destinations 
our_routes = {"SFO", "ORD", "ATL", "MIA", "LAX"}

# Flight destinations for the competitor airline
competitor_routes = {"ORD", "ATL", "LHR", "DXB", "BOS"}

# Step 1: Destinations that both airlines fly to (intersection)
common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)

# Step 2: Destinations unique to airline (difference)
unique_to_our_airline = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_our_airline)

# Step 3: Check if destinations that neither airline shares (symmetric difference)
unique_destinations = our_routes.symmetric_difference(competitor_routes)
print("Destinations that neither airline shares:", unique_destinations)