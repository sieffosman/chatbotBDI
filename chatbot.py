from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')  # Specify the template folder

# Initialize spaCy for NLP processing
import spacy

nlp = spacy.load("en_core_web_sm")

# Define FAQs and responses
faqs = {
    "hello": "Hello, I am MontyBot, how can I help you?",

    " ": "Hello, I am MontyBot, how can I help you?",
    
    "": "Hello, I am MontyBot, how can I help you?",

    "What is an innovation consultant?": "An innovation consultant helps businesses identify opportunities for growth and innovation.",
    
    "What services do you offer?": "We offer a range of services, including innovation strategy development, product ideation, and market analysis.",
    
    "What is Black Dog Innovation?": "Black Dog Innovation is a consultancy firm specializing in business and service design. They offer advisory services in various areas, including business strategy, design thinking, and lean startup methodologies.",
    
    "Who is Zunaid, and what is his role at Black Dog Innovation?": "Zunaid is a Business and Service Designer with over 8 years of advisory experience at Black Dog Innovation. He is passionate about combining business strategy and design thinking to create sustainable business models and value propositions. Zunaid also provides training in design thinking and lean startup methodologies.",
    
    "What services does Black Dog Innovation offer?": "Black Dog Innovation offers a range of services, including:\n\n- Business Design\n- Service Design\n- Capability Building\n- Coaching and Mentoring\nThey partner with organizations to create new business models, products, and services or enhance existing ones.",
    
    "What industries has Black Dog Innovation worked with?": "Black Dog Innovation has had the privilege of working with organizations across various industries, including the private, public, and charity sectors. They have expertise in Design Thinking, Lean Startup, and Agile Methodologies, delivering value to clients of all sizes and industries.",
    
    "Can you provide some client testimonials?": "Certainly! Here's what one of their clients had to say: 'In a rapidly changing world, having Zunaid as an innovation coach is like having a compass for navigating the unknown. He empowered our Group to embrace change and thrive in it.' - Matthias Stuwe, Head of Investment Steering and Management, Patrizia.",
    
    "Can you share some organizations that Black Dog Innovation has worked with?": "Black Dog Innovation has had the pleasure of collaborating with notable organizations, including The Economist, Google, and The National Grid.",
    
    "How can I get in touch with Black Dog Innovation?": "You can contact Black Dog Innovation by filling out the contact form on their website. Provide your name, email address, and a message, and they will get back to you.",

     "Tell me more about Zunaid's background": "Zunaid started his career in financial services and became a Chartered Accountant before transitioning into a strategy and innovation specialist. He excels at balancing organizational requirements with customer needs.",
    
    "What methodologies does Zunaid use in his work?": "Zunaid uses a combination of strategy, design thinking, and lean start-up methodologies in his work to create sustainable business models and customer-centric products and services.",
    
    "How did Black Dog Innovation get its name?": "Black Dog Innovation was inspired by a Tuesday morning coffee session and a dog named Monty. Zunaid decided to provide innovation services outside of London, and thus, Black Dog Innovation was born.",
    
    "Is Black Dog Innovation a registered company?": "Yes, Black Dog Innovation Ltd is a registered company with company number 14976088.",

    "What is Business Design at Black Dog Innovation?": "Business Design at Black Dog Innovation involves constructing sustainable business models with customers at their core.",
    
    "Tell me more about Service Design at Black Dog Innovation.": "Service Design at Black Dog Innovation focuses on creating exciting value propositions based on customer insights, which are validated through lean experimentation.",
    
    "What does Capability Building involve at Black Dog Innovation?": "Capability Building at Black Dog Innovation includes creating and delivering workshops and courses to up-skill individuals and teams, providing them with the knowledge and tools to successfully innovate.",
    
    "Can I get Coaching & Mentoring from Black Dog Innovation?": "Yes, Black Dog Innovation offers coaching and mentoring services. Zunaid is passionate about helping others get into innovation, and you can reach out to learn more about these services.",

     "Tell me more about the Ed Tech project": "The Ed Tech project involves reinvigorating the Ed Tech industry. It focuses on better meeting students' needs when learning online. Our approach includes stakeholder interviews, social listening, personas, journey mapping, ideation, and RICE prioritization. Please get in touch to receive my detailed portfolio.",
    
    "What is the Real Estate Leaders project about?": "The Real Estate Leaders project is designed to upskill leaders in the Real Estate industry while simultaneously creating an exciting new tool. We use facilitation, lean experimentation, problem framing, prototyping, and storytelling. Please get in touch to receive my detailed portfolio.",
    
    "Can you provide details about the Healthcare project?": "The Healthcare project aims to reimagine the Healthcare industry by harnessing existing in-person experience to democratize digital healthcare. Our approach includes competitor benchmarking, customer interviews, gap analysis, stakeholder interviews, and more. Please get in touch to receive my detailed portfolio.",

    "How can I get in touch with Black Dog Innovation?": "You can get in touch with us by filling out the form on our Contact page. Please provide your first name, last name, email, and a message. We're more than happy to have a chat, either in-person or over a coffee. Follow us on social media for updates.",

}

# Function to handle user queries
def chatbot_response(user_input):
    doc = nlp(user_input)
    
    for question, answer in faqs.items():
        similarity = doc.similarity(nlp(question))
        print(f"Similarity for '{question}': {similarity}")
        if similarity > 0.9:  # Increase the similarity threshold
            return answer

    return "I'm sorry, I couldn't understand your question. Please try again."

# Web route for chatbot
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Web route for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["user_input"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

