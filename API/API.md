# API Usage Guide: Alias Cluster Search

This API lets you search a cluster dataset by providing a query string (usually a name or alias), and it returns related direct and indirect aliases within the cluster.

---

## Base URL

http://127.0.0.1:5000


This is the local address where your Flask app is running. Replace `127.0.0.1` and port if deployed elsewhere.

---

## Endpoint: `/search`

### Method: `GET`

### Description

Searches the clusters for the query string and returns:

- The cluster name where the query matched
- A list of **direct aliases**: Names and aliases directly associated with the query
- A list of **indirect aliases**: Other names/aliases in the same cluster, but not directly linked to the query

---

### Example Request

Search for `"dragon bridge"`:

http://127.0.0.1:5000/search?query=dragon%20bridge

*Note:* Spaces should be URL-encoded as `%20`.

---

### Example Response (Success)

```json
{
  "cluster": "namecluster_123",
  "direct_aliases": [
    "DRAGONBRIDGE",
    "DRAGON_BRIDGE_ALIAS1",
    "DRAGON_BRIDGE_ALIAS2"
  ],
  "indirect_aliases": [
    "OTHER_ALIAS_1",
    "OTHER_ALIAS_2"
  ]
}
```
cluster: The cluster where the query was found.

direct_aliases: Names and aliases directly related to the query.

indirect_aliases: Other names/aliases in the same cluster but indirectly related.

## How the Search Works

- The API normalizes query and dataset strings by removing spaces, dashes, and underscores, and by converting to uppercase for case-insensitive matching.
- Matches are found if the normalized query equals the normalized name or any alias in the clusters.
- The API returns the first cluster that contains a match.
- Direct aliases include the matched name and its aliases.
- Indirect aliases include other names and aliases from the same cluster but not directly matched.

## Usage Tips

- URL-encode your query strings (spaces → `%20`).
- Try searching for both official names and aliases for comprehensive results.
- Example queries: `APT28`, `dragon bridge`, `dienet`.

## Running Locally

- Ensure you have Python installed.
- Install dependencies:
```bash
pip install flask
```
- Run the Flask app:

```bash
python search_api.py
```
- Access the API:

```bash
http://127.0.0.1:5000/search?query=your_query
```

## Example cURL Requests

```bash
curl "http://127.0.0.1:5000/search?query=dragon%20bridge"
```

```bash
curl "http://127.0.0.1:5000/search?query=APT28"
```

## Contact & Support

If you encounter any issues or have questions, feel free to open an issue or contact the maintainer.