# Introduction to Payment Initiation - Configuringpoapplication

> Source: https://docs.temenos.com/docs/Solutions/Payments/Orders/PI/Payment_Initiation_(PI)/Misc/Introduction_PI.htm#ConfiguringPOApplication

---

# Introduction to Payment Initiation

Updated On 12 April 2026 |
 16 Min(s) read

Feedback
Summarize

PAYMENT.ORDER (PO) application is an integral part of the Temenos Payment Solution, which is part of the Temenos Transact core banking suite. This handles order capture and management functionality, and supplements the payments processing engine, Temenos Payments Hub. The key features of PO application are as follows:

- Interfaces with a variety of payment initiation channels, both in interactive and Straight-Through Processing (STP) modes. Initiation channels include customer facing and electronic feeder channels (STP), bank’s branch or potentially in-house bank host systems that can raise a payment request.
- Performs order validation, pre-processing and storage until processing date.
- Performs manual repair and release for payments in exception.
- Helps in routing of the orders to appropriate payment system based on payment characteristics.
- Generates payment status reports, and customer advices and alert notifications
- Supports the following:
  - Payment capture for different types of clearings (such as RTGS, Automated Clearing Houses (ACH), Cross-Border and Instant Payments Clearings).
  - Popular clearing systems (such asTARGET2, SEPA using EBA, SEPA using RPSSCL, SEPA Instant, EQUENS, UK CHAPS, UK Faster payments, Hungary Instant (RT1), UK BACS, and SWISS RTGS).
  - Credit transfer, single and bulk payments, and a variety of payment types within credit transfers.
  - Customer payments and bank-to-bank transfers.
- Complies with ISO20022 payments messaging standards.
- Has a submodule of TPH that is offered by Temenos. However, banks can choose to use PO application as an independent module without TPH. In such installations, PO application interacts with bank’s non-Temenos payment systems to process payments captured or aggregated in PO application.
- Depends on Temenos Transact submodules to provide payment services. To know more, refer to PO application and associated Temenos Transact applications section.

## PO Application in Business Context

The following are the payment processing infrastructure of the bank.

Tap the  icon to enlarge the diagram for a better view.



[PO Application](#)

The functionalities of PO application are as follows:

- Receives payments using standard Temenos Transact interfaces, validates, enriches, and routes them to appropriate destination payment system.
- Sends the payment status back to initiating source in response to the acknowledgements received from the payment system.
- Generates payment advices as customer notifications.

[Payment Processing System](#)

The payment processing system (such as TPH or bank’s non-Temenos Payment system) validates, books and routes the payment to an appropriate clearing system. Payment instruction exchanges are in embedded mode when PO application operates with TPH, whereas, uses the standard message formats and interfaces in an external system. In-house payment requests are settled within the bank’s core banking, instead of sending it to clearing.

[Clearing Systems](#)

PO application supports the capture of payments, which are cleared by the following clearing systems:

| Clearing System | Description |
| --- | --- |
| Domestic | High-value RTGS payments, instant payments clearing systems or ACH that processes bulk payments |
| SWIFT | International payment message interchange |
| Cross-Border | Operate across borders, such as Pan European ACH |

[Bank Host Systems](#)

All systems in the bank that supplements payment processing, such as bank’s core banking system.

[API Support](#)

PO application can be accessed using APIs when deployed with Temenos Interaction Framework (IRIS) or third-party API gateway. This feature helps the bank to support PSD2 related open banking requirements, where the bank acts as a PISP or serves a PISP (as an account owning bank). The PO application supports the following APIs that supports both immediate and future dated payments:

| Release | API |
| --- | --- |
| Berlin Group Standards Release 1.3 | Payment Initiation |
| Payment Status |
| Payment Cancellation |
| Payment Completion |

This feature requires Temenos Transact PI module (PX) to be installed (Dependent modules are PZ and CK for processing permissions and third-party payment initiator validation).

[](#)[Status Updates to Source System](#)

The PAYMENT.ORDER (PO) application can receive payments from various Temenos Transact systems such as RTP, Forex, and so on. After the payment is completed, the PO application can update the status of the payment to these source systems. This can be configured in Payment Order Ps Mapping Rule setup.

## Configuring PO Application

PO application provides high level configuration with different aspects of payment capture.

[Payment Order Parameter](#)

This parameter allows the user to set characteristics of a PO application. The key parameters are as follows:

| Parameter | Description |
| --- | --- |
| Fraud Check Wait Response | Indicates whether the system must wait for a fraud check response or not when the underlying system is TPH, and the fraud check routine has been defined in the payment order product.  When POA and Transact are installed in the same instance, and payment processing is handled by standalone TPH, it is advised to handle the fraud check request and response in either TRANSACT POA or Standalone TPH. To achieve this, the FRAUD.CHECK.WAIT.RESPONSE parameter in the Payment Order Parameter table must be set as ‘Yes’. |
| Payment System | To process payments. The user can select the payment system to which the payment request needs to be sent. |
| Publish Special Events | To receive notifications for the following scenarios (if configured):  - Outward and inward payment status - Inward recall - Recall response - Recall rejected by clearing - Recall request overdue - Inward recall investigation   For example, inward recall notifies the client bank when Temenos Payments Hub (TPH) receives a recall from clearing.  This is applicable when running TPH as the payment system |
| Special Event Name | To receive notifications for specific special events. This is a multi-value field that is enabled, when *PublishSpecialEvents* field is set as ‘Yes’.  - If no events are selected in this field, the system sends notification for all special events. - If specific events are selected from the drop-down, the system sends notifications only for the selected special events.   The user needs to set the *PublishSpecialEvents* field as ‘Yes’ in both the scenarios.  The following special events (as multi-value) are available in the drop-down that notifies the client bank on:   - *Inward Recall* – Receipt of a recall request - *Recall Response* – Receipt of a response for a recall request sent previously - *Outward Payment Status* – Status of an outward payment - *Recall Rejected by Clearing* – Rejection of a recall request by clearing - *Recall Request Overdue* – Recall request sent becomes overdue - *Inward Payment Status* – Status of an inward payment received - *Inward Recall Investigation* – Investigate an unanswered recall request |
| Pre-Approved Payment | To skip balance check and fund reservation during payment processing. Following are the possible values:   - **Blank** - Balance check and fund reservation process are invoked during payment processing. - **Yes** - Balance check and fund reservation process are skipped during payment processing by POA and TPH. - **TPH** - Balance check and fund reservation process are skipped during payment processing only in TPH. This value can be used when POA and Transact are installed in the same instance and payment processing is handled by standalone TPH. |
| Pre Validated Account | To skip account validation and restriction checks during payment processing.  The user can set this parameter as 'Yes' only when Temenos Payments Hub is in standalone mode.  This scenario is applicable when accounts are maintained in an external DDA system and are not replicated in Temenos Payments Hub . Pre-validated payments initiated in Temenos Payments Hub must have their accounts validated externally prior to the payment initiation. Following are the possible values:   - **Blank** - Account validation and Account Restriction checks are invoked during payment processing. - **Yes** - Account validation and Account Restriction checks are skipped during payment processing by POA and TPH. - **TPH** - Account validation and Account Restriction checks are skipped during payment processing only in TPH. This value can be used when POA and Transact are installed in the same instance and payment processing is handled by standalone TPH. |
| Pre Determined FX | To skip determining the FX rates in Temenos Payments Hub .  The user must provide the exchange rate during payment initiation along with the payment amount and the currency equivalent amount. The user can set the parameter as 'Yes' only in Standalone mode. Following are the possible values:   - **Blank** - FX rate determination is invoked during payment processing. - **Yes** - FX rate determination is skipped during payment processing by POA and TPH. - **TPH** - FX rate determination is skipped during payment processing only in TPH. This value can be used when POA and Transact are installed in the same instance and payment processing is handled by standalone TPH. |
| Cancellable States | To process the cancellation request, the user can configure the payment order states eligible for cancellation . |

Read [Standalone Implementation Options](../../../../Payments/PP/Payments_Hub_(PP)/Standalone_Implementation_Options/Standalone_Implementation_Options.htm) section for more information on the deployment model.

[Country Level Configuration](#)

PO application are configured to adhere to payment rules that apply to payment identifiers of a given country (where the credit party holds an account). Following are the examples of country rules:

| Rule | Function |
| --- | --- |
| Allow or disallow IBAN | Validates whether an IBAN is allowed or disallowed in a payment. |
| Allow or disallow BIC | Validates whether a BIC of a beneficiary bank is allowed or disallowed in a payment. |
| Clearing code format | Mentions the format of clearing code for a specific country. System validates the clearing code format when initiating a payment to a country. |
| Allowed currencies | Inputs the list of currencies allowed to make a payment to a certain country. |

Payment products configured in PO application can be common across countries. However, country rules takes precedence (if set) over rules set at product level.

[Payment Order Product](#)

Every order is assigned a product attribute that determines the characteristics of the payment and the manner in which the payment is processed. Some of the generic products available in PO application are:



User chooses the Payment Order Product (during manual capture) or PO application automatically assigns it (based on the criteria defined by payment attributes). PO application products can also be based on message type (if there are specific requirements). For example, application product is UKFPS-SIP (Single Immediate Payments in UK FPS) or SEPA CT (SEPA Credit Transfer). Payment Product of PO application allows to set characteristics on how to capture, validate and process a payment order. Some of the key functionalities are as follows:

| Field | Functionality |
| --- | --- |
| *HolidayOption* | Indicates the country (holiday) to be considered when credit value date is calculated. |
| *Allow Iban* | Indicates if IBAN is allowed for a certain product.  Country rules take precedence while making a payment. |
| *Allow Bic* | Indicates if BIC is allowed for a certain product.  Country rules take precedence while making a payment. |
| *Allow Sort Code* | Indicates if Sort Code is allowed for a certain product.  Country rules take precedence while making a payment. |
| *Allow Fx* | Indicates if FX is allowed for a certain product.  When this field is checked, *Fx Float* is referred (to know the number of days taken for execution of the order involving FX). |
| *Warehouse Reqd* | Indicates if the future-dated payment request is warehoused in the PO application. |
| *Allowed Payment Ccy* | Indicates the list of currencies allowed to make a payment with the selected PO product. |
| *Charge Types* | Indicates the type of charge applicable for the order. |
| *Reachability check* | Indicates the type of reachability check. |
| *Check Transparency* | Indicates if simulation is allowed. |
| *Source System Id* | Indicates the system ID to be passed in the posting request when payment processing is completed in TPH. If this field is left blank, the system sends the default value ‘PP’ as the system ID in the posting request.  This field accepts any valid EB.SYSTEM.ID record that begins with ‘PP’. If configured, the value in the format <EB.SYSTEM.ID>\*<Ordering Reference> is defaulted to the *Context Value* field associated with CONTEXT.NAME>CORE-SOURCE.SYSTEM.ID at payment initiation.  If a valid value exists in the field, then the system must honour the value and must not overwrite with the default value.  Configuring this field also enables mapping of the *Ordering Reference* (contract reference) field value to the *Our Reference* field in the accounting entries. |

[API Hooks](#)

PO application allows to hook bank specific APIs to determine its product.

| API | Description |
| --- | --- |
| Product Determination API | Changes product dynamically based on payment information. For example, amount greater than 10,000 EUR is changed to TARGET2 payment product. |
| Charging Rule API | Determines whether a configured fee is applied or not. For example, the bank can choose not to charge cross-border fee, when the country is non-EU. |
| External Account lookup | Validates the account that is in a non-Temenos Transact database.  - Online capture – PO application provisions synchronous call facility to account management system - Offline capture (STP) – PO application offers asynchronous interaction facility with account management system. |
| Payment Validation | Allows custom validations that can be implemented during business validation stage of a payment order. |
| Connection API | Creates logic to connect to a specific payment system based on payment characteristics. For example, bulk payments sent to bulk payments engine. |
| Fraud Routine API | Allows local site-based API hooked to send payment information for fraud check. |

[Status Updates to Source System](#)

To update the status of the payment to the source system, the user has to provide the following configurations:

| Field | Description |
| --- | --- |
| *Source Mapping Api* | The API defined in this field must have the logic for one to one mapping from the PO application to the source application. |
| *Source Map Rule Api* | The API defined in this field determines whether the PO application must be mapped to the source system or not. The output of the *Source Map Rule API* field is compared with *Source Result Option* field. If the values are same, then the mapping is done from the PO application to the source system. If the values are different, then mapping is skipped. |



## Illustrating Model Parameters

The high-level configurations available in the Model Bank are given below:

| Parameter | Description |
| --- | --- |
| PAYMENT.ORDER.PARAMETER | This parameter table contains high-level payment order configuration at the company level. This application facilitates the definition of the Payment Connection method, whether Warehouse is supported and the number of days the Payment order needs to be maintained in live status before moving to history. |
| PAYMENT.ORDER.COUNTRY.RULES | This parameter table defines any country specific rules checking for Beneficiary country for outward payments. This takes precedence over similar definition in Payment Order Product. It also has the provision to set rules if IBAN, BIC, Sort Code or Clearing channels are applicable for specific countries. |
| PAYMENT.ORDER.PRODUCT | Payment features that are specific to a product are defined here. |

## Illustrating Model Products

Payment Initiation module captures the transaction details and forwards the instruction to the back office system configured in PAYMENT.ORDER.PARAMETER for further processing. It also applies some basic validations configured in the PAYMENT.ORDER.PRODUCT.

| Product | Description |
| --- | --- |
| Payment Initiation | Payment Connection Method in PAYMENT.ORDER.PARAMETER is set as Tps, so that all the payment initiated from PAYMENT.ORDER gets routed to TPH for further processing. |