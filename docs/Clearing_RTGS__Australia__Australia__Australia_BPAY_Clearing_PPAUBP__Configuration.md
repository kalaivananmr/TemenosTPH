# Configuring BPAY Clearing

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Australia/Australia/Australia_BPAY_Clearing_PPAUBP/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Australia > [BPAY](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm) > Configuration

- Australia;)
  - [BPAYBPAY](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm)
    - [Introduction](../../Australia/Australia_BPAY_Clearing_PPAUBP/Introduction.htm)
    - [Configuration](../../Australia/Australia_BPAY_Clearing_PPAUBP/Configuration.htm)
    - [Working with](../../Australia/Australia_BPAY_Clearing_PPAUBP/Working_with.htm)
    - [Tasks](../../Australia/Australia_BPAY_Clearing_PPAUBP/Tasks.htm)
    - [Outputs](../../Australia/Australia_BPAY_Clearing_PPAUBP/Outputs.htm)
  - [BECSBECS](../../Australia/Australia_BECS_PPBECS/Introduction.htm)
  - NPP Payments;)
  - BPAY Agency Banking;)
  - AURTGS Clearing;)
  - DE (BECS) Agency Banking;)
  - Clearing Directory Upload and Reachability Check;)

Payments

# Configuring BPAY Clearing

Updated On 07 August 2025 |
 2 Min(s) read

Feedback
Summarize

This section helps the user to configure the important parameters in BPAY.

## PAYMENT.ORDER(PO) Application for Payment Capture

The user can configure payment order product. To perform this, do the following actions:

1. Go to **Admin Menu**>**Payments Hub**>**Payment Order Admin Menu**>**Payment Order Product Setup**.
2. Enter the required details in the following fields:

   | Field | Description |
   | --- | --- |
   | *ID of the Product* | PO application product name |
   | *Description* | Enter Australia BPAY |
   | *Reachability Check* | Set to NA as reachability is not required for BPAY (as the validation of the billers are done by the clearing API call from Payment Order page) |
   | *Pay Through Beneficiary* | Set to Yes as payment is initiated for the biller through a beneficiary ID |
   | *Warehousing* | Set as Yes to warehouse the future-dated bill payments |

## Returns

The user can configure returns in PP.CLEARING.SETTING. To perform this, do the following actions:

1. Go to **Admin Menu**>**Payment Hub**>**Local Clearing**>**Clearing Setting**.
2. In the *Acceptance Days* field, enter the time frame within which an outward return request needs to be initiated.

## Clearing Cut-Off

The user can configure different cut-off times for BPAY payments. To perform this, do the following actions:

- Go to **Admin Menu**>**Payment Hub**>**Routing & Settlement**>**Channel Cutoff**.

In this topic

- [Configuring BPAY Clearing](#ConfiguringBPAYClearing)
  - [PAYMENT.ORDER(PO) Application for Payment Capture](#PAYMENTORDERPOApplicationforPaymentCapture)
  - [Returns](#Returns)
  - [Clearing Cut-Off](#ClearingCutOff)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Wednesday, June 17, 2026 2:21:49 PM IST