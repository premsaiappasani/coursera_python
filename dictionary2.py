def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group in group_dictionary.keys():
		# Now go through the users in the group
		for users in group_dictionary[group]:
		  lst = []
		  for group in group_dictionary.keys():
		    if users in group_dictionary[group] and users not in lst:
		      lst.append(group)
		  user_groups[users] = lst
	return user_groups
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary


print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
