import main_classes
import time

# Dictionary for keeping the areas under the routes which can be considered as 3 different maps/routes
Routes = {

    "neighborhood" : ["Home", "Front yard", "Parking lot", "Alley", "Bus stop",
                     "Playground", "Football field", "Public park", "Train station",
                     "Old warehouse", "Warehouse rooftop"],

    "downtown" : ["Apartment lobby", "Sidewalk", "Gas station", "Parking garage",
                 "Supermarket", "Food court", "Mall entrance", "Shopping mall",
                 "Escalators", "Rooftop terrace", "Mall rooftop"],

    "outdoors" : ["Campsite", "Forest trail", "Wooden bridge", "Hillside",
                 "Picnic area", "Lake shore", "Beach", "Boat dock",
                 "Cliff path", "Lighthouse", "Mountain peak"]
}




# Creates the items meant for the areas and returns a list of those items
def item_list_creator():
    item_1 = main_classes.Item("Banana peel", "Yellow, curved, slippery on the inside.", 30)
    item_2 = main_classes.Item("Candy wrapper", "Thin, shiny, crinkles when squeezed, twisted at both ends.", 5)
    item_3 = main_classes.Item("Wallet", "Brown, rectangular, folds in half, has slots inside", 200, False)
    item_4 = main_classes.Item("Old newspaper", "Gray, flat, small black marks, a date and headlines at the top.", 150)
    item_5 = main_classes.Item("Diamond necklace", "Shiny, cold to the touch, hangs from a chain, has a clear stone.",30, False)
    item_6 = main_classes.Item("Gold coin", "Round, yellow, heavy for its size, a face on one side.",31, False)
    item_7 = main_classes.Item("Empty cereal box", "Rectangular, light, bright colors, a list of numbers on the side.",90)
    item_8 = main_classes.Item("Soda can", "Cylindrical, metallic, cold, a ring on top.",15)
    item_9 = main_classes.Item("Dead battery", "Small cylinder, a metal end, a symbol printed near the top.",23)
    item_10 = main_classes.Item("Toilet paper", "White, soft, wound around a hollow core.",100)
    item_11 = main_classes.Item("Passport", "Small, rectangular, many thin pages, stamped in several places.",40, False)
    item_12 = main_classes.Item("Old shoe", "One of a pair, flexible, worn down on one side.",400)
    item_13 = main_classes.Item("Smartphone", "Flat, smooth, dark until touched.",190, False)
    item_14 = main_classes.Item("Watch", "Circular, metallic, repeats the same motion all day.",150, False)
    item_15 = main_classes.Item("Bread", "Firm on the outside, full of tiny holes on the inside.",70)
    item_16 = main_classes.Item("Cigarette butt", "Tiny, cylindrical, one end tan and spongy, the other end darkened and ashy.", 1)
    item_17 = main_classes.Item("Gold ring", "Small, circular, hollow in the middle, heavy for its size, tiny marks stamped inside.", 8, False)
    item_18 = main_classes.Item("Plastic bottle", "Light, clear, ridged at the bottom, a twist-on top, a paper band around the middle.", 25)
    item_19 = main_classes.Item("Credit card", "Thin, flat, rounded corners, a small metallic square on the front, a dark stripe on the back.", 5, False)
    item_20 = main_classes.Item("Used tissue", "Soft, white, crumpled into a ball, lightweight, damp in places.", 2)
    item_21 = main_classes.Item("Car keys", "Metal, toothed along one edge, a plastic head with small buttons, joined to a ring.", 60, False)
    item_22 = main_classes.Item("Chewing gum", "Small, gray, flat, sticky, stuck to a surface, holds the shape of teeth.", 3)
    item_23 = main_classes.Item("Pearl earrings", "Two small round beads, glossy white, each on a short metal post.", 4, False)
    item_24 = main_classes.Item("Pizza box", "Square, flat, cardboard, dark spots on the lid, a logo printed on top.", 180)
    item_25 = main_classes.Item("Gold bar", "Rectangular, yellow, far heavier than it looks, a number and a stamp pressed into the top.", 1200, False)
    item_26 = main_classes.Item("Torn sock", "Soft, stretchy, tube-shaped with a bend, a hole near one end.", 25)
    item_27 = main_classes.Item("Laptop", "Flat, hinged in two halves, one half covered in keys.", 200, False)
    item_28 = main_classes.Item("Egg shells", "Pale, curved fragments, thin and brittle, rough on the inside.", 20)
    item_29 = main_classes.Item("Camera", "Black, boxy and a round glass eye at the front.", 600, False)
    item_30 = main_classes.Item("Broken umbrella", "Long, folded, fabric stretched over thin metal ribs, one rib bent outward.", 350)
    return [item_1,item_2,item_3,item_4,item_5,item_6,item_7,item_8,item_9,item_10,item_11,item_12,item_13,item_14,item_15, item_16,item_17,item_18,item_19,item_20,
            item_21,item_22,item_23,item_24,item_25,item_26,item_27,item_28,item_29,item_30]

# Creates areas of the game and returns the list of those areas
# The first area is the lobby of an area where the player begins,
# so the items are there from 2nd area. This function runs a loop and creates each area with the relevant item (For example, 2nd area has the 1st item so indexes are different for calling each one)
# The areas of first route has items with index 0-9, second route has items with index 10-19 and third route has items with index 20-29
def area_list_creator(item_collection,area):
    area_list = []
    n = 0
    d = 10
    o = 20
    area_list.append(main_classes.Area(Routes[area][0]))

    for i in range(1,len(Routes[area])):

        if area == "neighborhood":
            area_list.append(main_classes.Area(Routes[area][i], item_collection[n]))
            n += 1
        elif area == "downtown":
            area_list.append(main_classes.Area(Routes[area][i], item_collection[d]))
            d += 1
        else:
            area_list.append(main_classes.Area(Routes[area][i], item_collection[o]))
            o += 1

    return area_list

# Creates a player object if there is no player object (Controlling creation of player object if it already exists from load)
def player_creator(player,user_name,area_list,powerup_inventory,area):
    if player == None:
        return main_classes.Player(user_name,area_list[0],powerup_inventory,area)

# Contains the powerup choice function which asks the player if they want to use their powerup and the code works accordingly and returns the selected powerup
def powerup_choice(powerup_inventory):

    powerup_decision_flag = False
    powerup_selector_flag = False

    while powerup_decision_flag == False:
        print("\nYour current powerups: ")
        for i in powerup_inventory:
            print(i)
        time.sleep(3)
        powerup_decision_raw = str(input("\nDo you want to use a powerup?\nEnter Y to use a powerup (!!Once you select Y, you will have to choose a powerup!!)\nEnter N to continue without powerup\n"))
        powerup_decision = powerup_decision_raw.lower()

        if powerup_decision == "y":

            powerup_decision_flag = True

            while powerup_selector_flag == False:
                powerup_selector_raw = str(input("\nEnter the powerup's name you want to use:\n"))
                powerup_selector = powerup_selector_raw.lower()

                if powerup_selector in powerup_inventory:
                    powerup_selector_flag = True
                    selected_powerup = powerup_selector
                    powerup_inventory.remove(selected_powerup)
                    return selected_powerup
                else:
                    print(f"\n{powerup_selector} is not available in your inventory!")

        elif powerup_decision == "n":
            powerup_decision_flag = True
            print("\nContinuing without powerup!")
            return ""

        else:
            print("\nInvalid Command! Try Again.")

# This function takes action according to the selected powerup
# A flag is used when the player has selected skip so it returns the boolean which is basically the flag which tells python to run code when the skip is not chosen.
def powerup_usage(selected_powerup,player):

    if selected_powerup == "reveal":
        print(f"\nThis item is {player.location.item.name}!")
        return False

    elif selected_powerup == "life":
        player.citizen_life += 10
        print(f"\nYour Citizen life has been increaded! Current Citizen life: {player.citizen_life}")
        return False
    
    else:
        print("\nItem skipped!")
        return True