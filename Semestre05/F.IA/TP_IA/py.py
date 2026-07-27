"""
Emojis : 
✅ ❌ ⚠️ ❗ ❕ ❓ ❔ ℹ️ ➕ ➖ ➗ ✖️ ➡️ ⬅️ ⬆️ ⬇️ 🔁 🔄 🔃 🔂 🔀 🔚 🔙 🔛 🔜 🔝
💻 🖥️ 🖱️ ⌨️ 🧮 ⚙️ 🧠 🧰 🧾 🗃️ 🗂️ 🗄️ 📂 📁 🪟 🧱
💬 🗯️ 💭 🗨️ 📨 📩 📧 ✉️ 🖊️ 🖋️ ✏️ 📝
😀 😃 😄 😁 😆 😅 😂 🤣 😊 😇 🙂
"""

MyResearchSpace = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A', 'E', 'F', 'G'],
    'E': [],
    'F': ['E', 'G'],
    'G': [],
}
class Node:
    def __init__(self, name, parent, action):
        self.name = name 
        self.parent = parent 
        self.action = action

    def display(self):
        print(f"Nom: {self.name} , Parent: {self.parent}.\nChemin : {self.action}.")

def getSolution(node):
    path = []
    current = node
    while current is not None:
        path.append(current.name)
        current = current.parent
    path.reverse()
    return path

# --- Main ---
G = Node(name='G',parent='F',action='explorer')
print(getSolution(G))  # Example usage