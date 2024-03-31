from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def get_llm_action(state: str) -> str:
    prompt = f"""You are playing a snake game on a 16x16 grid.
    The game is represented as a text-based grid, where 'H' represents the head of the snake,
    'B' represents the body of the snake, 'F' represents the food, and '-' represents an empty cell.
    The snake moves in the direction that its head is pointing.
    The snake can move up, down, left, or right. The snake cannot move through itself or the grid boundary.
    The game ends when the snake runs into itself or the grid boundary.
    The snake eats the food and grows longer when it moves onto the food.
    The food is then regenerated in a random location not occupied by the snake.
    Actions Available: [up, down, left, right].
    
    Few shot Exmaples:
    
    # Example 1
    state = 
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    --------HBB-----
    --------F-------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    
    # down
    
    # Example 2
    state = 
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    -------B--------
    -------B--------
    ------FH--------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    
    # left
    
    # Example 3
    state = 
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    -------F--------
    -------H--------
    -------B--------
    -------B--------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    ----------------
    
    # up
    """

    current_frame = f"""
    Here is the current state of the game:

    {state}
    
    Based on this state, what is the best action to take?
    NOTE: ONLY RETURN THE ACTION. DO NOT RETURN THE STATE.
    
    
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": current_frame
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    current_state = """
    H...............
    B...............
    B...............
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ..F.............
    ................
    """
    print(get_llm_action(current_state))
