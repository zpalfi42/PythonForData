class   calculator:
    """Calculator"""

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """_summary_

        Args:
            V1 (list[float]): _description_
            V2 (list[float]): _description_
        """
        dot_product = sum(V1[i] * V2[i] for i in range(len(V1)))
        print(f"Dot product is: {int(dot_product)}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """_summary_

        Args:
            V1 (_type_): _description_
        """
        add_vec = (float(V1[i] + V2[i]) for i in range(len(V1)))
        print(f"Dot product is: {list(add_vec)}")


    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """_summary_

        Args:
            V1 (list[float]): _description_
            V2 (list[float]): _description_
        """
        sous_vec = (float(V1[i] - V2[i]) for i in range(len(V1)))
        print(f"Dot product is: {list(sous_vec)}")