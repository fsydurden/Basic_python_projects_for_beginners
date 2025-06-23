weight = 10
g_cost = 0 #ground cost
d_cost = 0 #drone cost
#ground shipping
if weight <= 2:
  g_cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  g_cost = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  g_cost = weight * 4.00 + 20
else:
  g_cost = weight * 4.75 + 20

#premium
premium_ship = 125.00
print(f"We offer a premium shipping plan that has not weight limits. It costs only ${premium_ship}")

#drone shipping
if weight <= 2:
  d_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  d_cost = weight * 9.00
elif weight > 6 and weight <= 10:
  d_cost = weight * 12.00
else:
  d_cost = weight * 14.25

print(f"The Ground cost of shipping is ${round(g_cost, 2)} and Drone cost of shipping is ${round(d_cost, 2)}.")
