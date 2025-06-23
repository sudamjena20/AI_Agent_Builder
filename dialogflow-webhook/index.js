const express = require('express');
const bodyParser = require('body-parser');
const sgMail = require('@sendgrid/mail');

const app = express();
app.use(bodyParser.json());

// Replace with your actual SendGrid API key
sgMail.setApiKey('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');

app.post('/', async (req, res) => {
  const tag = req.body.fulfillmentInfo.tag;

  if (tag === 'send-confirmation-email') {
    const params = req.body.sessionInfo.parameters;
    const msg = {
      to: params.email,
      from: 'jenasudam950@gmail.com', // Must be a verified sender in SendGrid
      subject: 'Appointment Confirmation',
      text: `Hi ${params.name}, your appointment for a ${params.property_type} on ${params.datetime} is confirmed.`,
    };

    try {
      await sgMail.send(msg);
      res.json({
        fulfillment_response: {
          messages: [{ text: { text: ['Confirmation email sent.'] } }],
        },
      });
    } catch (error) {
      console.error(error);
      res.json({
        fulfillment_response: {
          messages: [{ text: { text: ['Failed to send email.'] } }],
        },
      });
    }
  } else {
    res.json({
      fulfillment_response: {
        messages: [{ text: { text: ['No matching tag.'] } }],
      },
    });
  }
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
