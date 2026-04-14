import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [21, 23, 34, 54],
    "City": ["New York", "Singapore", "Tokyo", "Gloucester"],
}

df = pd.DataFrame(data)


def get_person_by_name(df, name):
    """
    Search for a person in the DataFrame by name.

    Args:
        df: Pandas DataFrame with person data
        name: Name to search for (string)

    Returns:
        Series with matching person's data, or None if not found
    """
    result = df[df["Name"] == name]

    if result.empty:
        return None

    return result.iloc[0]


# Example usage
person = get_person_by_name(df, "Bob")
print(person)
