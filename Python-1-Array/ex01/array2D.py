def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list and return the truncated version.

    Args:
        family (list): A 2D list to be sliced.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        list: The sliced 2D list.

    Raises:
        TypeError: If 'family' is not a list of lists or if 'start'/'end'
        are not integers.
        ValueError: If sublists in 'family' are not of the same length.
    """
    # Validate that 'family' is a list of lists
    if not isinstance(family, list) or not all(isinstance(row, list)
                                               for row in family):
        raise TypeError("The 'family' parameter must be a list of lists.")

    # Validate that 'start' and 'end' are integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("'start' and 'end' must be integers.")

    # Check that all sublists have the same length
    if len(family) > 0:
        row_length = len(family[0])
        if not all(len(row) == row_length for row in family):
            raise ValueError(
                "All sublists in 'family' must have the same length."
            )

    # Print the original shape
    original_shape = (len(family), len(family[0]) if family else 0)
    print(f"My shape is : {original_shape}")

    # Apply slicing
    sliced_family = family[start:end]

    # Print the new shape
    new_shape = (
        len(sliced_family),
        len(sliced_family[0]) if sliced_family else 0
    )
    print(f"My new shape is : {new_shape}")

    return sliced_family
