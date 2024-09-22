const cors = require("cors");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(cors());

// POST endpoint
app.post("/bfhl", (req, res) => {
  const { data } = req.body;

  if (!data || !Array.isArray(data)) {
    return res.status(400).json({
      is_success: false,
      user_id: "Saransh_Saxena_16102003",
      email: "sm1772@srmist.edu.in",
      roll_number: "RA2111003030030",
      numbers: [],
      alphabets: [],
      highest_alphabet: [],
    });
  }

  const numbers = data.filter((item) => !isNaN(item));
  const alphabets = data.filter(
    (item) => isNaN(item) && /^[a-zA-Z]$/.test(item)
  );
  const highestAlphabet = alphabets
    .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
    .slice(-1)[0];

  res.json({
    is_success: true,
    user_id: "Shivay_Garg_16102003",
    email: "sr0614@srmist.edu.in",
    roll_number: "RA2111003030110",
    numbers,
    alphabets,
    highest_alphabet: highestAlphabet ? [highestAlphabet] : [],
  });
});


// GET endpoint
app.get("/bfhl", (req, res) => {
  res.status(200).json({ operation_code: 1 });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
