# Introduction to Fraud Check - Top

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/HongKong/Payment_Initiation_(PI)/Fraud_Check/Introduction.htm#top

---

2. [Payments](../../../../content/payments.html)

- Hong Kong;)

Payments

# Introduction to Fraud Check

Updated On 07 August 2025 |
 8 Min(s) read

Feedback
Summarize

The PAYMENT.ORDER (PO) application is an integral part of the Temenos Payment Solution in the Temenos Temenos Transact Core Banking suite. This can invoke fraud check on the orders during order processing. Fraud check is the process of checking the customer and order details in the restricted list (such as Office of Foreign Assets Control (OFAC)) to prevent fraud or perform Anti Money Laundering (AML) checks. It is initiated on all orders received in PO application from any electronic channels or manually captured in the PO application. This check can be enabled or disabled at business product level. For example, the user can configure fraud check on international payments but not on domestic payments products.

When enabled, the PO application prepares a fraud check request and sends it to the fraud engine. The request has standard set of fields from the order, as configured in Temenos Transact. However, additional attributes of the order can be sent after making necessary local development. The PO application further processes the order based on the responses received from the fraud check system. Following are the possible responses:

| Response | Description |
| --- | --- |
| Success | Order is processed forward. |
| Failed | Order is cancelled when the response indicates potential fraud. |
| Timeout | Timeout responses are taken positively or negatively based on the configuration in PO application. |

## Invoking Fraud Check

After payment is received in PO and authorised:

- The fraud check request is sent to an engine (if configured). To know more on the invocation of fraud check activity in the processing flow, refer to [PO application Basic Functions](../Misc/Introduction_PI.htm#top) section.
- The request is held for the fraud check response by placing it in ‘Fraud Check’ status.

PO application receives the following responses from the fraud engine:

| Status | Description |
| --- | --- |
| Success | If the fraud engine does not identify any problem, it sends a Success response. The PO application updates the *Order Status* to ‘Fraud Check Complete’ and *Fraud Check Indicator* to ‘Success’, and moves the order to the next state. |
| Fail | If the fraud engine identifies a potential fraud with the order sent, it sends a Fail response. The PO application updates the *Order Status* to ‘Fraud Check Failed’ and *Fraud Check Indicator* to ‘Failed’, and marks the Payment Order to ‘Cancel Order’. |
| Timeout | If an order is sent to fraud engine and a timeout response is received, PO application updates the *Order Status* to ‘Fraud Check Timeout’ and *Fraud Check Indicator* to ‘Timeout’. The PO application further processes or cancels the payment order based on the pre-defined configuration. |
| Hold | If the response received is ‘HOLD’, the *Order Status* remains in ‘FraudCheck’ and waits for final response. |
| Pending | If an order is sent to fraud engine and the response is awaited, PO application updates the Fraud Check Indicator to ‘Pending’ when parallel processing is enabled. |

## Payment Order States for Fraud Check Workflow

The Payments Order states are as given below.

| State | FraudCheckIndicator | Description |
| --- | --- | --- |
| FraudCheck | Not updated | Payment is sent to fraud check system. |
| FraudCheckComplete | Success | Positive fraud check response is received and the payment is ready for execution. |
| FraudCheckFailed | Failed | Negative fraud check response is received and the payment is cancelled. |
| FraudCheckTimeout | Timeout | Fraud check is timed out and the payment is either continued or cancelled based on configuration. |
| FraudCheckBypassed | Bypassed | Fraud check is bypassed and the payment processing is continued. |

## Fraud Check Timeout Handling

If the fraud check response is not received within the configured time, *Fraud Check Indicator* is updated to Timeout. The payment order state is updated to ‘FraudCheckTimeout’. Based on the configuration, the payment is either continued or cancelled.

A timed-out Payment Order may later receive a delayed response from the Fraud Check system. In such a scenario, *Fraud Check Indicator* is updated to reflect the response received from the fraud check system, such as Success, Failed, or Hold.

## Bypassing Fraud Check in Payment Orders

If *Fraud Check Required* is set to Bypass while the payment is processed and *Fraud Check Indicator* is set to Bypassed.

## Fraud Check Execution for Warehoused Payments

When a payment is received with a future execution date, the payment order is warehoused. At this stage, fraud check is not done.

Fraud check is done when a payment order is released from the warehouse.

## Interfacing to Fraud Engine

The fraud engine can be a Temenos Transact module (Temenos screen) or third-party system. PO application can be integrated to external fraud engines based on the standard Temenos Transact Integration Framework (IF), using an ESB and a bank-specific ‘fraud routine’ attached to it. The routine defines the order data sent to fraud engine. This can be set specific to a Temenos Transact company, and hence, different routines can be attached to different companies for performing fraud check.

If different Temenos Transact companies employ different fraud engines, Temenos provides:

- A standard interfacing routine, when the fraud engine is Temenos screen.
- The API routine for all other engines to send the fraud check request to fraud engine, which is created at the project implementation level.

The fraud engine sends the responses using standard interfacing (through ESB and Temenos OFS methods). To know more, refer to Temenos Transact [Interfacing](../Interfaces_and_Message_Standards/Introduction.htm#top) section.

## Parallel Processing

PO application can initiate a fraud check and simultaneously send the order for further processing to payment system, without waiting for the fraud check response. This feature helps to increase the speed of processing, especially during the process of instant payments.

This is applicable only when the underlying payment system is Temenos Payment Hub (TPH).

TPH processes the payment and then moves it to awaiting queue until accounting and external payment generation. Based on the response from the fraud engine, the PO application intimates TPH on the status, and TPH releases or cancels the payment, accordingly.

## Updating Fraud Check Indicator Manually

The PO application allows the user to manually update the status of the *Fraud Check Indicator*, when there is a temporary or permanent issue that leads to fraud engine failing to send a response. The possible statuses are available: Success, Failed or Timeout. The PO application processes the payment based on the response from the user. To know more, refer to Processing Description section.

## Installing PO Application with Temenos Screen

PO application has pre-integrated interfaces with the Temenos Screen system, thus, does not require an integration activity during implementation.

In this topic

- [Introduction to Fraud Check](#IntroductiontoFraudCheck)
  - [Invoking Fraud Check](#InvokingFraudCheck)
  - [Payment Order States for Fraud Check Workflow](#PaymentOrderStatesforFraudCheckWorkflow)
  - [Fraud Check Timeout Handling](#FraudCheckTimeoutHandling)
  - [Bypassing Fraud Check in Payment Orders](#BypassingFraudCheckinPaymentOrders)
  - [Fraud Check Execution for Warehoused Payments](#FraudCheckExecutionforWarehousedPayments)
  - [Interfacing to Fraud Engine](#InterfacingtoFraudEngine)
  - [Parallel Processing](#ParallelProcessing)
  - [Updating Fraud Check Indicator Manually](#UpdatingFraudCheckIndicatorManually)
  - [Installing PO Application with Temenos Screen](#InstallingPOApplicationwithTemenosScreen)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:17:17 PM IST