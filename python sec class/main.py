party_items : list[str] = ["samosa","pani puri","chocolate","roll"]
party_items.append("ice cream")
party_items.extend(["chips", "cookies"])

party_items.remove("pani puri")
print(party_items)

party_friends :list[str]=["affan","wali","abdul","zain","basit"]
#muja lagta ha basit ko remove karna chaya or huzaifa ko add so let see
party_friends.remove("basit")
party_friends.append("huzaifa")
print(party_friends)