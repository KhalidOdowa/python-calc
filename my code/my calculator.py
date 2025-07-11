function calculator() {}
console.log("Welcome to Simple Calculator!");

    while (true) {
        console.log("\nSelect operation:");
        console.log("1. Add");
        console.log("2. Subtract");
        console.log("3. Multiply");
        console.log("4. Divide");
        console.log("5. Exit");

        const choice = prompt("Enter choice (1/2/3/4/5): ").trim();

        if (choice === '5') {
            console.log("Thanks for using the calculator!");
            break;
        }

        if (['1', '2', '3', '4'].includes(choice)) {
            try {
                const num1 = parseFloat(prompt("Enter first number: "));
                const num2 = parseFloat(prompt("Enter second number: "));

                if (isNaN(num1) || isNaN(num2)) {
                    console.log("Invalid input. Please enter numbers only.");
                    continue;
                }

                if (choice === '1') {
                    console.log("Result:", (num1 + num2).toFixed(2));
                } else if (choice === '2') {
                    console.log("Result:", (num1 - num2).toFixed(2));
                } else if (choice === '3') {
                    console.log("Result:", (num1 * num2).toFixed(2));
                } else if (choice === '4') {
                    if (num2 === 0) {
                        console.log("Error: Cannot divide by zero.");
                    } else {
                        console.log("Result:", (num1 / num2).toFixed(2));
                    }
                }
            } catch (error) {
                console.log("An error occurred. Please try again.");
            }
        } else {
            console.log("Invalid input, please try again.");
        }
    }
}
