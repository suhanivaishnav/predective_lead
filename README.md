# 🔮 Predictive Lead Conversion Using Metadata

In many businesses, especially in B2B industries, the **lead conversion rate remains as low as 1.5%**, despite high volumes of incoming leads. This results in wasted marketing effort, lower ROI, and missed revenue opportunities.

This project leverages **Artificial Intelligence** to analyze **lead metadata**—such as source, region, industry, device, and engagement patterns—to predict the **probability of conversion**. This enables organizations to **prioritize, personalize, and optimize** their lead engagement strategies.

---

## 🎯 Project Goals

- ✅ **Prioritize high-value leads**
- ✅ **Personalize follow-ups** based on probability
- ✅ **Optimize marketing and sales workflows**
- ✅ **Reduce acquisition costs and improve ROI**

---

## 🧠 Tech Stack

- **Language**: Python
- **Libraries**: Pandas, Scikit-learn, Joblib
- **Web Interface**: Streamlit
- **Intel AI Optimization**:
  - Intel® Extension for Scikit-learn
  - Intel® oneAPI AI Analytics Toolkit

---

## 📊 Dataset Overview

**Source**: Simulated lead metadata for Tara Metal Industry  
**Size**: 300 records  
**Features**:
- `lead_source` – Web, Email, Referral, etc.
- `industry` – Automobile, Construction, Engineering, etc.
- `region` – India-North, India-South, etc.
- `num_interactions` – Count of touchpoints (emails/calls)
- `time_since_last_contact` – Days since last interaction
- `device_type` – Desktop, Mobile, Tablet
- `converted` – Target label (1 = Converted, 0 = Not Converted)

---

## 🛠️ Folder Structure

predictive-lead-conversion/
├── app/
│ └── app.py
├── data/
│ └── tara_metal_leads.csv
├── models/
│ └── model.pkl (generated after training)
├── src/
│ ├── train_model.py
│ └── predict.py
├── requirements.txt
└── README.md

## 🚀 How to Run

1. **Install dependencies**  

pip install -r requirements.txt
Train the model

python src/train_model.py
Launch the web app

streamlit run app/app.py
Upload CSV file
Use the UI to upload a dataset and view predicted conversion probabilities.

📈 Model Performance
Accuracy: 87%

ROC-AUC: 0.91

Precision: 86%

Recall: 84%

📌 Future Improvements
CRM integration (Salesforce, HubSpot)

NLP analysis of lead communication

Custom lead scoring visualizations

Dashboard for conversion insights

👩‍💻 Project Author
Suhani Vaishnav
📧 vaishnavsuhani2004@gmail.com

🧠 Powered by Intel AI Tools
Optimized with Intel® Extension for Scikit-learn and Intel® AI Analytics Toolkit for faster model training and prediction performance.
