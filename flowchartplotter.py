from graphviz import Digraph

# Create a flowchart using Graphviz
flowchart = Digraph("90_Day_Strategy", format="png")
flowchart.attr(rankdir="LR", size="15,10")

# Phase 1 Nodes
flowchart.node("P1", "Phase 1: Discovery, Validation, and Building Momentum", shape="box", style="filled", color="lightblue")
flowchart.node("MR", "Market Research & Validation", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("PP", "Pilot Partnerships", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("MVP", "Define MVP Scope", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("BM", "Branding & Messaging", shape="ellipse", style="filled", color="lightgrey")

# Phase 2 Nodes
flowchart.node("P2", "Phase 2: Build, Test, and Iterate", shape="box", style="filled", color="lightblue")
flowchart.node("MVPDev", "MVP Development", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("BT", "Beta Testing with Partners", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("MO", "Marketing & Outreach", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("FP", "Funding Preparation", shape="ellipse", style="filled", color="lightgrey")

# Phase 3 Nodes
flowchart.node("P3", "Phase 3: Prepare for Launch and Scale", shape="box", style="filled", color="lightblue")
flowchart.node("MVPOpt", "MVP Optimisation", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("PE", "Partnership Expansion", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("UA", "User Acquisition & Awareness", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("IS", "Infrastructure Scaling", shape="ellipse", style="filled", color="lightgrey")
flowchart.node("SP", "Strategic Plan for Year 1", shape="ellipse", style="filled", color="lightgrey")

# Connections for Phase 1
flowchart.edge("P1", "MR")
flowchart.edge("P1", "PP")
flowchart.edge("P1", "MVP")
flowchart.edge("P1", "BM")

# Connections for Phase 2
flowchart.edge("P2", "MVPDev")
flowchart.edge("P2", "BT")
flowchart.edge("P2", "MO")
flowchart.edge("P2", "FP")

# Connections for Phase 3
flowchart.edge("P3", "MVPOpt")
flowchart.edge("P3", "PE")
flowchart.edge("P3", "UA")
flowchart.edge("P3", "IS")
flowchart.edge("P3", "SP")

# Sequential Flow Between Phases
flowchart.edge("MR", "P2", lhead="cluster_P1")
flowchart.edge("MVPDev", "P3", lhead="cluster_P2")

# Render the flowchart
file_path = "/mnt/data/90_day_strategy_flowchart"
flowchart.render(file_path, cleanup=True)

file_path + ".png"
