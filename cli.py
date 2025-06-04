from hashring import ConsistentHashRing

def main():
    ring = ConsistentHashRing(replicas=100)

    print("📡 Consistent Hash Ring CLI")
    print("Commands:")
    print("  add <node>         - Add a node")
    print("  remove <node>      - Remove a node")
    print("  get <key>          - Get node for a key")
    print("  show               - Show all nodes")
    print("  exit               - Quit")

    while True:
        command = input(">>> ").strip().split()

        if not command:
            continue

        cmd = command[0].lower()

        if cmd == "add" and len(command) == 2:
            node = command[1]
            ring.add_node(node)
            print(f"✅ Added node: {node}")

        elif cmd == "remove" and len(command) == 2:
            node = command[1]
            ring.remove_node(node)
            print(f"❌ Removed node: {node}")

        elif cmd == "get" and len(command) == 2:
            key = command[1]
            node = ring.get_node(key)
            print(f"🔑 Key '{key}' maps to node: {node}")

        elif cmd == "show":
            print("🧩 Current nodes:")
            for node in sorted(ring.nodes):
                print(f" - {node}")
            print()

        elif cmd == "exit":
            print("👋 Exiting.")
            break

        else:
            print("⚠️ Invalid command or usage.")

if __name__ == "__main__":
    main()
