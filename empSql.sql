-- Create the `employee` table
CREATE TABLE employee (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
);

-- Create the `employee_UIN` table
CREATE TABLE employee_UIN (
    ID INT PRIMARY KEY,
    UIN VARCHAR(20)
);

-- Insert sample data into `employee`
INSERT INTO employee (ID, Name, Age) VALUES
(1, 'Alice', 23),
(2, 'Bob', 28),
(3, 'Charlie', 22),
(4, 'Diana', 24);

-- Insert sample data into `employee_UIN`
INSERT INTO employee_UIN (ID, UIN) VALUES
(1, 'UIN123'),
(2, 'UIN456'),
(3, 'UIN789'),
(4, 'UIN101');

-- Query to generate the required list
SELECT eu.UIN, e.Name
FROM employee e
JOIN employee_UIN eu ON e.ID = eu.ID
WHERE e.Age < 25
ORDER BY e.Name ASC, e.ID ASC;
