
"use client";
import { useState } from "react";

export default function Home() {
  const [cart, setCart] = useState("");
  const [totalPrice, setTotalPrice] = useState<number | null>(null);
  const [error, setError] = useState("");

  const handleCheckout = async (
    event: React.MouseEvent<HTMLButtonElement>
  ) => {
    event.preventDefault();

    if (cart.trim() === "") {
      setError("Cart cannot be empty!");
      setTotalPrice(null);
      return;
    }
    if (/[a-z]/.test(cart)) {
      setError("Cart cannot contain lowercase letters!");
      setTotalPrice(null);
      return;
    }
    setError("");
    setTotalPrice(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/checkout/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ cart }),
      });

      const data = await response.json();
      if (data.total_price !== undefined) {
        setTotalPrice(data.total_price);
      }
    } catch (err) {
      setError("An error occurred. Please try again.");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">
      <div className="bg-white rounded-2xl shadow-lg p-8 w-full max-w-md">
        <h1 className="text-2xl font-bold text-center text-gray-800 mb-6">
          🛒 Supermarket Checkout
        </h1>

        <div className="mb-4">
          <label
            htmlFor="cart"
            className="block text-sm font-medium text-gray-700"
          >
            Enter Cart (e.g., AAABBD):
          </label>
          <input
            type="text"
            id="cart"
            name="cart"
            value={cart}
            onChange={(e) => setCart(e.target.value)}
            required
            className="mt-2 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
            placeholder="AAABBD"
          />
        </div>

        <button
          id="checkout-button"
          onClick={handleCheckout}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-4 rounded-lg transition duration-300"
        >
          Calculate Total
        </button>

        {totalPrice !== null && (
          <div className="mt-6 text-center text-xl text-green-600 font-bold">
            Total Price: ₹{totalPrice}
          </div>
        )}

        {error && (
          <div className="mt-4 text-center text-red-600 font-medium">
            {error}
          </div>
        )}
      </div>
    </div>
  );
}
