# 🚀 Food Delivery Time Prediction

This project predicts **food delivery time (in minutes)** based on the **age of the delivery partner, ratings of previous deliveries, and total distance** using an **LSTM (Long Short-Term Memory) model**. The model is trained using a dataset from **Kaggle** and deployed using **Streamlit Cloud**.

## 📌 Project Overview
- 💊 **Dataset**: [Food Delivery Dataset](https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset?select=train.csv)  
- 🧠 **Model**: LSTM (Long Short-Term Memory)  
- 🌐 **Live Demo**: [Food Delivery Time Prediction App](https://fooddeliverytime-cxrqljvinteekh44c7aemo.streamlit.app/)  
- 🖥️ **Tech Stack**: Python, TensorFlow, Keras, Streamlit, NumPy  

---

## 📂 Dataset Details
The dataset contains:
- `Age of Delivery Partner` (integer)  
- `Ratings of Previous Deliveries` (float)  
- `Total Distance` (integer)  
- `Delivery Time` (target variable, in minutes)  

---

## 🚀 How to Use the App?
1. **Visit the Live App**: [Click Here](https://fooddeliverytime-cxrqljvinteekh44c7aemo.streamlit.app/)  
2. Enter:
   - **Age of Delivery Partner** (18-65)
   - **Ratings of Previous Deliveries** (1.0 - 5.0)
   - **Total Distance** (in km)  
3. Click **"Predict Delivery Time"** to get the estimated time in minutes.  

---

## 🛠 How to Run Locally?
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/food-delivery-prediction.git
cd food-delivery-prediction
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Download Dataset
Download the dataset from [Kaggle](https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset?select=train.csv) and place it in the project directory.

### 4️⃣ Train the Model
Run the following script to train and save the LSTM model:
```sh
python train_model.py
```

### 5️⃣ Run the Streamlit App
```sh
streamlit run streamlit_app.py
```
Now, open the **local URL** displayed in the terminal.

---


## 📄 Requirements
Create a **`requirements.txt`** file and include:
```
streamlit
tensorflow
numpy
pandas
```

---


## 🤝 Contributing
If you’d like to contribute:
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Create a Pull Request  

---

## 🐝 License
This project is licensed under the **MIT License**.

---

## 📧 Contact
For questions or collaborations, reach out to:    
🔗 [GitHub](https://github.com/knight22-21)  
🔗 [LinkedIn](https://www.linkedin.com/in/krishna-tyagi-/)  

---
🚀 **Enjoy Predicting Food Delivery Times!** 🎯
