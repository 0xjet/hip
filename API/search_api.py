from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)

# Load your cluster data once at startup
output_dir = "../3-nameclusters"
input_path = os.path.join(output_dir, "nameclusters.json")

with open(input_path, 'r') as f:
    cluster_data = json.load(f)

def normalize_string(s):
    """Normalize alias or name for comparison."""
    return s.replace(" ", "").replace("-", "").replace("_", "").upper()

def find_cluster_by_alias(query):
    norm_query = normalize_string(query)
    print(f"Searching for normalized query: {norm_query}")

    for cluster_name, items in cluster_data.items():
        print(f"Checking cluster: {cluster_name}")

        # Collect all entries (name and alias) in normalized form, mapping back to original strings
        name_to_item = {}
        alias_to_item = {}

        if not "alias" in items[0]: #singleton cluster found
            singleFullName = normalize_string(items[0]['name']) #UNK:TURKHACKTEAM
            singleName = singleFullName.split(":")[-1]          #TURKHACKTEAM
            vendor = singleFullName.split(":")[0]               #UNK

            if norm_query == singleName:

                return {
                    "cluster": cluster_name,
                    "direct_aliases": [singleFullName],
                    "indirect_aliases": []  # empty list for consistency
                }
        else:
            for item in items:
                name_norm = normalize_string(item['name']).split(":")[-1]  # handle splitting safely
                alias_list = item['alias'] if isinstance(item['alias'], list) else [item['alias']]
                alias_norm_list = [normalize_string(a).split(":")[-1] for a in alias_list]

                name_to_item[name_norm] = item
                for anorm in alias_norm_list:
                    alias_to_item[anorm] = item

            # Find all matching items in this cluster (name or alias matches)
            matching_items = []
            for item in items:
                name_norm = normalize_string(item['name']).split(":")[-1]
                alias_list = item['alias'] if isinstance(item['alias'], list) else [item['alias']]
                alias_norm_list = [normalize_string(a).split(":")[-1] for a in alias_list]

                if norm_query == name_norm or norm_query in alias_norm_list:
                    matching_items.append(item)

            if not matching_items:
                continue

            # Direct aliases = all names and aliases of matching items
            direct_aliases = set()
            for mi in matching_items:
                direct_aliases.add(mi['name'])
                if isinstance(mi['alias'], list):
                    direct_aliases.update(mi['alias'])
                else:
                    direct_aliases.add(mi['alias'])

            # Indirect aliases = all other names and aliases in cluster excluding direct aliases
            indirect_aliases = set()
            for item in items:
                if item in matching_items:
                    continue  # skip matched items
                indirect_aliases.add(item['name'])
                if isinstance(item['alias'], list):
                    indirect_aliases.update(item['alias'])
                else:
                    indirect_aliases.add(item['alias'])

            # Remove any possible empty or None entries
            direct_aliases = {a for a in direct_aliases if a}
            indirect_aliases = {a for a in indirect_aliases if a and a not in direct_aliases}

            return {
                "cluster": cluster_name,
                "direct_aliases": sorted(direct_aliases),
                "indirect_aliases": sorted(indirect_aliases)
            }

    print("No match found")
    return None



@app.route('/')
def home():
    """Serve the frontpage."""
    return render_template('index.html')

    
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if not query:
        return jsonify({"error": "Please provide a search query parameter, e.g. /search?query=APT28"}), 400

    result = find_cluster_by_alias(query)
    if not result:
        return jsonify({"message": f"No results found for '{query}'"}), 404

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)



#http://127.0.0.1:5000/search?query=dragon%20bridge