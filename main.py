from core.pendency_tracker import PendencyTracker

def main():
    pendency_tracker = PendencyTracker()

    pendency_tracker.startTracking(1112, ["UPI", "Karnataka", "Bangalore"])
    pendency_tracker.startTracking(2451, ["UPI", "Karnataka", "Mysore"])
    pendency_tracker.startTracking(3421, ["UPI", "Rajasthan", "Jaipur"])
    pendency_tracker.startTracking(1221, ["Wallet", "Karnataka", "Bangalore"])

    print(pendency_tracker.getCounts(["UPI"]))
    print(pendency_tracker.getCounts(["UPI", "Karnataka"]))
    print(pendency_tracker.getCounts(["UPI", "Karnataka","Bangalore"]))
    print(pendency_tracker.getCounts(["Bangalore"]))

    pendency_tracker.startTracking(4221, ["Wallet", "Karnataka", "Bangalore"])
    pendency_tracker.stopTracking(1112)
    pendency_tracker.stopTracking(2451)

    print(pendency_tracker.getCounts(["UPI"]))
    print(pendency_tracker.getCounts(["Wallet"]))
    print(pendency_tracker.getCounts(["UPI", "Karnataka", "Bangalore"]))



if __name__ == '__main__':
    main()


