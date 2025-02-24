import pickle

def inspect_pickle(filepath):
    """Loads and inspects the contents of a pickle file."""
    try:
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
            print("Pickle file loaded successfully!")
            print("Data type:", type(data))
            print("Data:", data)  # Be careful with large objects!

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

inspect_pickle('voting_prediction_model.pkl')