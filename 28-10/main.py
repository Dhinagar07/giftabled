from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

expenses = {}
next_id = 1

@app.post("/expenses")
def add_expense(expense_data: dict):
    global next_id
    description = expense_data.get("description", "")
    amount = expense_data.get("amount")
    category = expense_data.get("category", "")
    
    if not description or str(description).strip() == "":
        raise HTTPException(status_code=400, detail="Description cant  empty")
    try:
        amount_num = float(amount)
    except:
        raise HTTPException(status_code=400, detail="Invalid amount")
    if amount_num <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")
    
    expense_id = next_id
    next_id += 1
    expenses[expense_id] = {
        "expense_id": expense_id,
        "description": str(description).strip(),
        "amount": amount_num,
        "category": str(category).strip() if category else ""
    }
    return {"message": "Expense added successfully", "expense": expenses[expense_id]}

@app.get("/expenses")
def get_expenses():
    return list(expenses.values())

@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, expense_data: dict):
    if expense_id not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    if "description" in expense_data:
        desc = expense_data["description"]
        if not desc or str(desc).strip() == "":
            raise HTTPException(status_code=400, detail="Description cannot be empty")
        expenses[expense_id]["description"] = str(desc).strip()
    
    if "amount" in expense_data:
        try:
            amount_num = float(expense_data["amount"])
        except:
            raise HTTPException(status_code=400, detail="Invalid amount")
        if amount_num <= 0:
            raise HTTPException(status_code=400, detail="Amount must be greater than zero")
        expenses[expense_id]["amount"] = amount_num
    
    if "category" in expense_data:
        expenses[expense_id]["category"] = str(expense_data["category"]).strip()
    
    return {"message": "Expense updated successfully", "expense": expenses[expense_id]}

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    if expense_id not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    del expenses[expense_id]
    return {"message": "Expense deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
