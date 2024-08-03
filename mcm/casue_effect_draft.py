import matplotlib.pyplot as plt
import networkx as nx
import textwrap

# 创建一个有向图
G = nx.DiGraph()

# 添加节点和节点的标签
nodes = {
    "Pm": "Male Lampreys (Pm)",
    "Pf": "Female Lampreys (Pf)",
    "S": "Other Species (S)",
    "F": "Food Resources (F)",
    "E_stability": "Ecosystem Stability (E_stability)"
}

G.add_nodes_from(nodes)

# 添加边以及边的标签
edges = [
    ("Pf", "Pm", {"label": "Reproduction"}),
    ("Pm", "F", {"label": "-Demand"}),
    ("Pf", "F", {"label": "-Demand"}),
    ("S", "F", {"label": "-Demand"}),
    ("F", "S", {"label": "+Growth"}),
    ("Pm", "E_stability", {"label": "+/- Impact"}),
    ("Pf", "E_stability", {"label": "+/- Impact"}),
    ("S", "E_stability", {"label": "+/- Impact"}),
    ("F", "E_stability", {"label": "+Availability"}),
]
G.add_edges_from([(e[0], e[1]) for e in edges])

edge_labels = {(e[0], e[1]): e[2]['label'] for e in edges}

# 位置
pos = nx.spring_layout(G)

# # 自定义图形尺寸，保持节点尺寸不变
plt.figure(figsize=(8, 7))  # 设置图形尺寸为20x15英寸

# 处理节点标签的自动换行
wrapped_labels = {node: textwrap.fill(label, width=10) for node, label in nodes.items()}

# 绘制节点，保持node_size为8000
nx.draw_networkx_nodes(G, pos, node_size=7000, node_color="lightblue")

# 绘制边
nx.draw_networkx_edges(G, pos, edgelist=edge_labels.keys())

# 绘制节点标签
nx.draw_networkx_labels(G, pos, labels=wrapped_labels, font_size=10)

# 绘制边标签
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.5)

# 显示图
plt.axis('off')
plt.title("Ecosystem Model Causal Relationship Diagram")
plt.tight_layout()  # 优化整个布局
plt.show()