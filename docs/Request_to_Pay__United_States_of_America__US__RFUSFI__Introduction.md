# Introduction to Fednow Request For Payment

> Source: https://docs.temenos.com/docs/Solutions/Payments/Request_to_Pay/United_States_of_America/US/RFUSFI/Introduction.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   United States of America > Fednow Request For Payment > Introduction

- United States of America;)
  - Fednow Request For Payment;)
    - [Introduction](../../US/RFUSFI/Introduction.htm)
    - [Configuration](../../US/RFUSFI/Configuration.htm)
    - [Working with](../../US/RFUSFI/WorkingWith.htm)
    - [Tasks](../../US/RFUSFI/Tasks.htm)
    - [Outputs](../../US/RFUSFI/Outputs.htm)

Payments

# Introduction to Fednow Request For Payment

Updated On 10 July 2025 |
 25 Min(s) read

Feedback
Summarize

Fednow Request For Payment (RFP) module is enabled to receive and process an incoming RFP Request (pain.013) message from FedNow clearing and send out the receipt acknowledgement (admi.007) message for successful receipt of RFP (pain.013) message and respond with the following messages.

- RFP (pain.014) message with the status RCVD if the received RFP (pain.013) message file is accepted (file level acceptance) by the module successfully.
- RFP (pain.014) message with the status PRES if the received RFP (pain.013) message is viewed by the end customer via channel for the 1st time.
- RFP (pain.014) message with the status ACTC if the received RFP request is approved by the end customer or by the bank user ( on behalf of the end customer).
- RFP (pain.014) message with the status RJCT if the received RFP request is rejected by the end customer or by the bank user ( on behalf of the end customer).

RFP module is also enabled to receive and process an incoming RFP cancellation request (camt.055) message from FedNow clearing and send out the receipt acknowledgement (admi.007) message for successful receipt of RFP cancellation request (camt.055) message and automatically respond with the following messages, based on the status of underlying RFP order.

- RFP cancellation request response (camt.029) message with status code RJCR if the received RFP cancellation request is rejected by the system
- RFP cancellation request response (camt.029) message with status code "CNCL" if the received RFP cancellation request is accepted by the system.

## RFP Request and RFP Request Response - RFP Receive Only

This functionality enables banks to receive and process an incoming RFP Request (pain.013) message from the FedNow clearing and send out the receipt acknowledgement (admi.007) message for a successful receipt of the RFP (pain.013) message and respond with the RFP (pain.014) message.

Banks are able to receive and process the receipt acknowledgement (admi.007) message if the sent RFP response message is validated at the FedNow clearing and payee bank, and handle the incoming message reject (admi.002) from the FedNow clearing due to a rejection of the sent RFP (pain.014) message. Also, banks are able to receive the payment status request (pacs.028) message and send out the receipt acknowledgement (admi.007) message for a successfully received pacs.028 message. TPH will send the latest sent RFP (pain.014) message as a response to the received (pacs.028) message based on the status of the RFP order.

New configurations, mappings and process flows have been released to support the FedNow RFP message processing.

## RFP Cancellation Request and RFP Cancellation Request Response - RFP Cancellation Request Receive

This functionality allows banks to receive and process the incoming RFP cancellation request (camt.055) messages from FedNow clearing and send out the receipt acknowledgement (admi.007) messages for successful receipt of RFP cancellation request (camt.055) messages and automatically respond with RFP cancellation request response (camt.029) messages, based on the status of underlying RFP order.

Banks are able to receive and process the receipt acknowledgement (admi.007) message if the sent RFP cancellation request response (camt.029) message is validated at the FedNow clearing and Payee bank, and handle the incoming message reject (admi.002) from the FedNow clearing due to rejection of the sent RFP cancellation request response (camt.029) message. This functionality allows the payer bank to process the incoming RFP cancellation request (camt.055) message and send the admi.007 acknowledgement message for the received pain.013 message.

For all the sent RFP cancellation request response (camt.029) message, the debtor agent will receive the incoming receipt acknowledgement (admi.007) message from the FedNow clearing and Creditor agent.

New configurations, mappings and process flows have been released to support the FedNow RFP message processing.

## RFP Information Request and Response

This functionality allows the debtor agent (payer bank) to generate the outgoing Information Request (camt.026) message for the received RFP request and receive a receipt acknowledgement (admi.007) message if the sent IR (camt.026) message is validated successfully and also handle the incoming Message Reject (admi.002) if the sent IR (camt.026) message got rejected at FedNow clearing. For the sent IR (camt.026) message the system will have the ability to receive and process the following response messages:

- Information Request Response (camt.029) message with the status code PDNG.
- Information Request Response (camt.029) message with the status code IPAY.
- Information Request Response (camt.029) message with the status code IDUP.
- Information Request Response (camt.029) message with the status code NINF.
- Information Request Response (camt.029) message with the status code INFO.
- Additional Payment Information (camt.028) message.

For all the received response messages, the debtor agent will send the receipt acknowledgement (admi.007) message to the FedNow clearing and Creditor agent (via FedNow clearing). Upon receiving Information Request Response with (camt.029) message with the code INFO, the module will be enabled to receive Addition Payment Information (camt.028) message.

Also, this functionality enables banks to amend the RFP order based on the received Additional Payment Information (camt.028) message.

RFP module is enabled to generate outward Information Request (camt.026) message to the FedNow clearing for the received RFP request (bank user can initiate an IR or IR can be initiated based on the received API response from the end customer channel).

This functionality enables the debtor agent (payer bank) to generate the outgoing Information Request (camt.026) message for the received RFP request.

An information request message is used by sender FI and receiver FI or on behalf of the end customer to communicate with another FedNow Participant for more information on a previously sent or received RFP (pain.013) message.

The Information Request message (camt.026) is received by the debtor agent of the underlying RFP pain.013 message, to convey the details about any of the following reasons. On successfully receiving the camt.026 message, the system automatically sends out receipt ack message (admi.007) to clearing.

- Any additional information
- Missing information
- Incorrect information
- Possible duplicate
- Anti Money Laundering Request

For the received IR (camt.026) message, the bank user can respond with the following messages. The response can be sent either through the browser screen or based on the API request received from the customer channel.

- Information Request Response (camt.029) message with status (PDNG/ NINF/ INFO/ IPAY/ IDUP)
- Additional Payment Information (camt.028) message

For the sent response (camt.029/camt.028) message, the system can receive either a positive acknowledgement message - "receipt acknowledgement" (admi.007) or a nack message (admi.002) from the FedNow service.

Consider a scenario where,

1. An end user of a software application receives an RFP (through their bank) from the vendor of a software product for a sum of Rs.100 and with the payer name as ‘SAAM’.
2. After receiving the RFP request, the end customer received an information request message (camt.026) stating that the payer name mentioned in the RFP is to be considered as ‘SAM’.
3. The Debtor bank responds to the received IR in the form of IRR (camt.029 - INFO) followed by an additional payment information message (camt.028) stating that payer name will be considered as ‘SAM’ instead of ‘SAAM’.
4. The bank user can now amend the payer's name in the received RFP order as ‘SAM’ (based on the sent camt.028 message).

To view the received information request, navigate to **User menu** > **Payments** > **Request to Pay** > **RTPs Received** > **RTP Received Enquiries** > **All Received** > **View IR Detail**

To respond to the received information request, navigate to **User menu** > **Payments** > **Request to Pay** > **Information Request** > **Information Request Received** > **Pending** > **Respond**

To amend the RFP order, navigate to **User menu** > **Payments** > **Request to Pay** > **Information Request** > **Information Request Received** > **Processed** > **Amend RTP**

Read the [Introduction to Information Request](https://docs.temenos.com/docs/Solutions/Payments/Payments/RF/Request_to_Pay/Information_Request/Introduction.htm) section of the Request to Pay guide for more information on the information request message.

## Outward RFP Request and Response

The creditor agent (payer bank) is enabled to generate the outgoing RFP (pain.013) message either by the bank user or based on the received API request from end customer channel.

For the RFP (pain.013) message, the system will have the ability to receive and process the following response messages:

- RFP response pain.014 message with RCVD status as soon as the RFP sent has been successfully accepted in the payers system.
- RFP Response pain.014 message with PRES status, once the sent RFP is successfully viewed by the end customer via channel
- RFP Response pain.014 message with ACTC status as soon as the RFP sent has been successfully accepted in the payers system.
- RFP Response pain.014 message with RJCT status as soon as the RFP sent is rejected by the payer.

The creditor bank is enabled to automatically initiate outward payment status request (pacs.028) message for the outward RFP (pain.013) message, if the system does not receive RFP response (pain.014) message within the set time in the scheme.

For the sent RFP Request for payment pain.013 message/ Investigation pacs.028 message , the creditor bank RFP module will be enabled to receive and process the incoming receipt acknowledgement (admi.007) message and process Message Reject (admi.002) from the clearing.

## Outward RFP Cancellation Request and RFP Cancellation Request Response

The creditor agent is enabled to generate the outgoing RFP cancellation request (camt.055) message and receive the following clearing response.

- Receipt acknowledgement (admi.007) message if the sent camt.055 message got processed successfully at the clearing
- Message Reject (admi.002) if the sent camt.055 message got rejected at the clearing.

For the sent RFP cancellation request, the system will receive RFP cancellation request response (camt.029) with status code (RJCR / CNCL).

## RFP Inward Information Request and Response

The creditor agent (payee bank) is enabled to receive the incoming Information Request (camt.026) message for the sent RFP (pain.013) request and send a receipt acknowledgement (admi.007) message. For the received IR (camt.026) message, the bank user responds with the following messages (the response can be send either via browser screen or API request):

- Information Request Response (camt.029) message with status (PDNG / NINF/ INFO / IPAY / IDUP).
- Additional Payment Information (camt.028) message.

For the sent IRR (camt.029) / Additional Payment Information (camt.028) message system is eligible to receive and process the following messages, receipt acknowledgement (admi.007) if the sent messages get accepted at clearing & payee bank and message reject (admi.002) if the sent message got rejected at the clearing layer due to technical validation failure. For responding with additional payment information (camt.028) message the system will allow the bank user to amend the RFP order

For example: A software service provider firm (namely: TMS) has raised a RFP request to all their clients at the end of the billing cycle via their bank. For the sent RFP (pain.013) message the firm TMS receives a IR (camt.026) from one of their client asking for a change in the expiry date. For the received IR, software firm responds with IRR (camt.029-INFO) followed by additional payment information (camt.028) stating the expiry date can be changed to 30-01-2025 instead of 25-01-2025. Now this information has to be updated in the respective RFP order, hence the software firm (or the bank user on behalf of them) can amend this RFP order and change the expiry date based on the information sent in the (camt.028) message.

## Reachability check for RFP (pain.013) and PP Message (pacs.008/pacs.004)

The banks are enabled to check for reachability of the receiver FedNow participant, when an outward payment (pacs.008) / return payment (pacs.004) / request for payment (pain.013) message is initiated via API or via browser.

## Incoming Zero Dollar RFP

The debtor agent (payer bank) is enabled to receive and process the incoming zero dollar FedNow RFP (pain.013) message and send a receipt acknowledgement (admi.007) message after the incoming RFP (pain.013) message is validated successfully. The RFP module sends either of the following FedNow RFP response messages to the FedNow service.

- RFP (pain.014) message with the status ACTC if the received RFP request process all the validations successfully.
- RFP (pain.014) message with the status RJCT if the received RFP request is declined due to validation failure.

For all the sent RFP response (pain.014) message, the debtor agent receives the incoming receipt acknowledgement (admi.007) message from the FedNow clearing & Creditor agent. The module handles the incoming Message reject (admi.002) from the FedNow clearing if the sent response RFP (pain.014) is not validated successfully at the FedNow clearing.

## Outgoing Zero Dollar RFP

Zero-dollar RFP message is initiated by the debtor agent to check if the creditor agent is enabled to receive and act upon it. While it is not required to use zero-dollar RFP messages prior to send actual RFPs, it is recommended to improve the overall biller/customer experience with RFP onboarding.

For example, at the end of every month an spare part's manufacturer may request their corresponding bank (ex: TPH bank) to raise RFP to all of its customer's. TPH bank can initiate a zero dollar RFP (before initiating normal RFP) to all the banks (of specified customers) to check the banks readiness to receive & take action. Also to check if the account number provided is valid or not.

Banks can initiate the new FedNow zero dollar RFP via the following path: “User Menu -> Payments -> Request To Pay -> Initiate Request To Pay (RTP) -> US FedNow Zero Dollar RFP Request".

## Outgoing Information Request for Outgoing RFP

Information request (camt.026) message can be sent for the underlying outward RFP (pain.013) message, to convey any of the following information:

- Any additional information
- Missing information
- Incorrect information
- Possible duplicate
- Anti Money Laundering Request

For the sent camt.026 message FedNow clearing sends either positive acknowledgment (admi.007) message or negative acknowledgment (admi,002) message due to rejection of the sent message. Additionally system receives and processes the following response from another FedNow participant via FedNow service.

- Information Request Response (camt.029) with status codes: "PDNG," "IPAY," "IDUP," "NINF," "INFO."
- Additional Payment Information (camt.028) with status code "ADDL."

After the receipt of camt.029 / camt.028 message system automatically sends out admi.007 message to the FedNow service and bank user amends the RFP order based on the information received in (camt028) message.

- For example: A software service provider firm (ABC Services) sends RFP request to all its end customer's at the end of every billing period via the bank (Name: Temenos Bank). The firm ABC has wrongly inputted the RFP amount as 10000/- now they wanted to inform all its end customer to pay for a different amount which is Rs 7000/-, this information is communicated to all the end users by initiating (camt.026) message. For the sent camt.026 message temenos bank receives IRR (camt.029) message with INFO status followed by additional payment information (camt.028) message containing the following information "RFP will be accepted for the amount Rs 7000/-". Temenos bank user amends the underlying RFP order amount fields as 7000/-

Refer to [Introduction to Information Request](../../Request_to_Pay/Information_Request/Introduction.htm) section of **Request to Pay** guide for more information on the information request message.

Enquiry to initiate the IR request is **User menu > Payments > Request To Pay > RTPs Sent > RTP Sent Enquiries > All Sent > Raise IR**.

Enquiry to view the initiated IR request is **User menu > Payments > Request to Pay > Information Request > Information Request Sent> Awaiting Response**.

Enquiry to view the initiated IR request after the receipt of final response is **User menu > Payments > Request to Pay > Information Request > Information Request Sent> Processed**.

## Outward RFP Cancellation Request and RFP Cancellation Request Response

The creditor agent is enabled to generate the outgoing RFP cancellation request (camt.055) message and receive the following clearing response.

- Receipt acknowledgment (admi.007) message if the sent camt.055 message got processed successfully at the clearing
- Message Reject (admi.002) if the sent camt.055 message got rejected at the clearing

For the sent RFP cancellation request the system will receive RFP cancellation request response (camt.029) with any of the status code and sends receipt acknowledgment (admi.007) message to the clearing

- PDCR - Sent cancellation request is pending at the payer bank
- RJCR - Payer bank have rejected the sent cancellation request
- CNCL - Payer bank have approved the sent cancellation request

Navigation to initiate new cancellation request is via: **User menu > Payments > Request To Pay > RTPs Sent > RTP Sent Enquiries > Initiate Recall >Recall Request**

Navigation to view the completed cancellation request is via: **User menu > Payments > Request To Pay > RTPs Sent > RTP Sent Enquiries > Recalled**

Refer to [Introduction To Recall](../../Request_to_Pay/RtP_Recall/Introduction.htm) section of Request to Pay guide for more information on the working of RFP cancellation request.

For Example: Electronic manufacturing company (KTM) raises an RFP request to one of its client for an amount of 500 USD via their bank (Temenos bank). After raising the request they have noticed the payment for the product sold has already been received. KTM has instructed the temenos bank to raise an cancellation request (camt.055) for the already sent (pain.013) message. Now for the sent cancellation request temenos bank receives RFP cancellation request response camt.029 with CNCL status meaning the sent RFP message has been cancelled by the payer bank.

## FedNow RFP Character Set Support

Bank user initiate's the following RFP related messages by inputting allowed special characters in the free text fields, system generates the outward xml file with the inputted special character and sends it to FedNow clearing.

- RFP (pain.013) message
- RFP Response (pain.014 - RJCT) message
- RFP Cancellation Request (camt.055)

For example: At the end of every month an spare part's (TEKIO) manufacturer may request their corresponding bank (ex: TPH bank) to raise RFP to all of its customer's. Now TPH bank user will initiate RFP request to all the customer's by inputting the field (End to End Identification) as "TEKIOÑ@" system should process & generate the outward pain.013 xml message to the FedNow clearing.

The list of supported special characters,

| Character Code | Character | Description |
| --- | --- | --- |
| 32 | SP | Space |
| 33 | ! | Exclamation mark |
| 34 | " | Double quotes (or speech marks) |
| 35 | # | Number sign |
| 36 | $ | Dollar |
| 37 | % | Per cent sign |
| 38 | & | Ampersand |
| 39 | ' | Single quote |
| 40 | ( | Open parenthesis (or open bracket) |
| 41 | ) | Close parenthesis (or close bracket) |
| 42 | \* | Asterisk |
| 43 | + | Plus |
| 44 | , | Comma |
| 45 | - | Hyphen-minus |
| 46 | . | Period, dot, or full stop |
| 47 | / | Slash or divide |
| 48 | 0 | Zero |
| 49 | 1 | One |
| 50 | 2 | Two |
| 51 | 3 | Three |
| 52 | 4 | Four |
| 53 | 5 | Five |
| 54 | 6 | Six |
| 55 | 7 | Seven |
| 56 | 8 | Eight |
| 57 | 9 | Nine |
| 58 | : | Colon |
| 59 | ; | Semicolon |
| 60 | < | Less than (or open angled bracket) |
| 61 | = | Equals |
| 62 | > | Greater than (or close angled bracket) |
| 63 | ? | Question mark |
| 64 | @ | At sign |
| 65 | A | Uppercase A |
| 66 | B | Uppercase B |
| 67 | C | Uppercase C |
| 68 | D | Uppercase D |
| 69 | E | Uppercase E |
| 70 | F | Uppercase F |
| 71 | G | Uppercase G |
| 72 | H | Uppercase H |
| 73 | I | Uppercase I |
| 74 | J | Uppercase J |
| 75 | K | Uppercase K |
| 76 | L | Uppercase L |
| 77 | M | Uppercase M |
| 78 | N | Uppercase N |
| 79 | O | Uppercase O |
| 80 | P | Uppercase P |
| 81 | Q | Uppercase Q |
| 82 | R | Uppercase R |
| 83 | S | Uppercase S |
| 84 | T | Uppercase T |
| 85 | U | Uppercase U |
| 86 | V | Uppercase V |
| 87 | W | Uppercase W |
| 88 | X | Uppercase X |
| 89 | Y | Uppercase Y |
| 90 | Z | Uppercase Z |
| 91 | [ | Opening bracket |
| 92 | \ | Backslash |
| 93 | ] | Closing bracket |
| 94 | ^ | Caret - circumflex |
| 95 | \_ | Underscore |
| 96 | ` | Grave accent |
| 97 | a | Lowercase a |
| 98 | b | Lowercase b |
| 99 | c | Lowercase c |
| 100 | d | Lowercase d |
| 101 | e | Lowercase e |
| 102 | f | Lowercase f |
| 103 | g | Lowercase g |
| 104 | h | Lowercase h |
| 105 | i | Lowercase i |
| 106 | j | Lowercase j |
| 107 | k | Lowercase k |
| 108 | l | Lowercase l |
| 109 | m | Lowercase m |
| 110 | n | Lowercase n |
| 111 | o | Lowercase o |
| 112 | p | Lowercase p |
| 113 | q | Lowercase q |
| 114 | r | Lowercase r |
| 115 | s | Lowercase s |
| 116 | t | Lowercase t |
| 117 | u | Lowercase u |
| 118 | v | Lowercase v |
| 119 | w | Lowercase w |
| 120 | x | Lowercase x |
| 121 | y | Lowercase y |
| 122 | z | Lowercase z |
| 123 | { | Opening brace |
| 124 | | | Vertical bar |
| 125 | } | Closing brace |
| 126 | ~ | Equivalency sign - tilde |

| Character Code | Character | Description |
| --- | --- | --- |
| 192 | À | Latin capital letter A with grave |
| 193 | Á | Latin capital letter A with acute |
| 194 | Â | Latin capital letter A with circumflex |
| 195 | Ã | Latin capital letter A with tilde |
| 196 | Ä | Latin capital letter A with diaresis |
| 197 | Å | Latin capital letter A with ring above |
| 198 | Æ | Latin capital letter AE |
| 199 | Ç | Latin capital letter C with cedilla |
| 200 | È | Latin capital letter E with grave |
| 201 | É | Latin capital letter E with acute |
| 202 | Ê | Latin capital letter E with circumflex |
| 203 | Ë | Latin capital letter E with diaresis |
| 204 | Ì | Latin capital letter I with grave |
| 205 | Í | Latin capital letter I with acute |
| 206 | Î | Latin capital letter I with circumflex |
| 207 | Ï | Latin capital letter I with diaresis |
| 208 | Ð | Latin capital letter ETH |
| 209 | Ñ | Latin capital letter N with tilde |
| 210 | Ò | Latin capital letter O with grave |
| 211 | Ó | Latin capital letter O with acute |
| 212 | Ô | Latin capital letter O with circumflex |
| 213 | Õ | Latin capital letter O with tilde |
| 214 | Ö | Latin capital letter O with diaresis |
| 215 | × | Multiplication sign |
| 216 | Ø | Latin capital letter O with slash |
| 217 | Ù | Latin capital letter U with grave |
| 218 | Ú | Latin capital letter U with acute |
| 219 | Û | Latin capital letter U with circumflex |
| 220 | Ü | Latin capital letter U with diaresis |
| 221 | Ý | Latin capital letter Y with acute |
| 222 | Þ | Latin capital letter THORN |
| 223 | ß | Latin small letter sharp s - ess-zed |
| 224 | à | Latin small letter a with grave |
| 225 | á | Latin small letter a with acute |
| 226 | â | Latin small letter a with circumflex |
| 227 | ã | Latin small letter a with tilde |
| 228 | ä | Latin small letter a with diaresis |
| 229 | å | Latin small letter a with ring above |
| 230 | æ | Latin small letter ae |
| 231 | ç | Latin small letter c with cedilla |
| 232 | è | Latin small letter e with grave |
| 233 | é | Latin small letter e with acute |
| 234 | ê | Latin small letter e with circumflex |
| 235 | ë | Latin small letter e with diaresis |
| 236 | ì | Latin small letter i with grave |
| 237 | í | Latin small letter i with acute |
| 238 | î | Latin small letter i with circumflex |
| 239 | ï | Latin small letter i with diaresis |
| 240 | ð | Latin small letter eth |
| 241 | ñ | Latin small letter n with tilde |
| 242 | ò | Latin small letter o with grave |
| 243 | ó | Latin small letter o with acute |
| 244 | ô | Latin small letter o with circumflex |
| 245 | õ | Latin small letter o with tilde |
| 246 | ö | Latin small letter o with diaresis |
| 247 | ÷ | Division sign |
| 248 | ø | Latin small letter o with slash |
| 249 | ù | Latin small letter u with grave |
| 250 | ú | Latin small letter u with acute |
| 251 | û | Latin small letter u with circumflex |
| 252 | ü | Latin small letter u with diaresis |
| 253 | ý | Latin small letter y with acute |
| 254 | þ | Latin small letter thorn |
| 255 | ÿ | Latin small letter y with diaresis |

In this topic

- [Introduction to Fednow Request For Payment](#IntroductiontoFednowRequestForPayment)

- [RFP Request and RFP Request Response - RFP Receive Only](#RFPRequestandRFPRequestResponseRFPReceiveOnly)
- [RFP Cancellation Request and RFP Cancellation Request Response - RFP Cancellation Request Receive](#RFPCancellationRequestandRFPCancellationRequestResponseRFPCancellationRequestReceive)
- [RFP Information Request and Response](#RFPInformationRequestandResponse)
- [Outward RFP Request and Response](#OutwardRFPRequestandResponse)
- [Outward RFP Cancellation Request and RFP Cancellation Request Response](#OutwardRFPCancellationRequestandRFPCancellationRequestResponse)
- [RFP Inward Information Request and Response](#RFPInwardInformationRequestandResponse)
- [Reachability check for RFP (pain.013) and PP Message (pacs.008/pacs.004)](#ReachabilitycheckforRFPpain013andPPMessagepacs008pacs004)
- [Incoming Zero Dollar RFP](#IncomingZeroDollarRFP)
- [Outgoing Zero Dollar RFP](#OutgoingZeroDollarRFP)
- [Outgoing Information Request for Outgoing RFP](#OutgoingInformationRequestforOutgoingRFP)
- [Outward RFP Cancellation Request and RFP Cancellation Request Response](#OutwardRFPCancellationRequestandRFPCancellationRequestResponse1)
- [FedNow RFP Character Set Support](#FedNowRFPCharacterSetSupport)

Related topics:

- [Abbreviations](Abbreviations.htm)
- [APIs](API.htm)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:36:21 PM IST