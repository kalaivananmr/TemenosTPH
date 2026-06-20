# Configuring Lebanon RTGS

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Lebanon/Lebanon/Lebanon_RTGS_PPLBNC/Configuration.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Lebanon > [Lebanon RTGS](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm) > Configuration

- Lebanon;)
  - [Lebanon RTGS Lebanon RTGS](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm)
    - [Introduction](../../Lebanon/Lebanon_RTGS_PPLBNC/Introduction.htm)
    - [Configuration](../../Lebanon/Lebanon_RTGS_PPLBNC/Configuration.htm)
    - [Working with](../../Lebanon/Lebanon_RTGS_PPLBNC/Working_with.htm)
    - [Tasks](../../Lebanon/Lebanon_RTGS_PPLBNC/Tasks.htm)
    - [Outputs](../../Lebanon/Lebanon_RTGS_PPLBNC/Outputs.htm)
  - [Lebanon Cheque Clearing Lebanon Cheque Clearing](../../Lebanon/Lebanon_Clearing_PPLBCQ/Introduction.htm)

Payments

# Configuring Lebanon RTGS

Updated On 06 July 2023 |
 3 Min(s) read

Feedback
Summarize

TPH bank can be a direct participant of BDL-RTGS (Lebanon RTGS). The channel through which payment is routed determines the participation type in the TPH. TPH comes with configuration records already available for Lebanon RTGS. The below sections help in configuring the important parameters to Lebanon RTGS.

## Direct Participant

Lebanon is an RTGS clearing system, hence, it needs to be configured accordingly. This enables the user to configure a direct participant. To perform this, do the following:

1. Go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing**.

The below screenshot displays the configuration.



2. Update the following attributes that determine the uniqueness and behaviour of clearing payments:

| Attribute | Description |
| --- | --- |
| *Swift Based* | Set to Y, as Lebanon RTGS is a SWIFT-based clearing. |
| *Settlement Type* | Set to Gross, as Lebanon RTGS is an RTGS settlement system. |
| *Service Identifier* | Set to DLP to populate in Tag 103 of the outgoing message, which denotes a Lebanon RTGS payment. |
| *Clearing Country Code* | Set to LB, which is the country code for Lebanon. |
| *RTGS system* | Set to Y, as Lebanon RTGS is a RTGS system. |
| *Skip Reachability* | Set to Y, when reachability check is not required (as Lebanon RTGS is a RTGS system). |
| *Clearing File Transaction Indicator* | Set to T, as Lebanon RTGS is transaction based. |
| *Clearing Currency* | Set to LBP, as TPH currently supports only LBP currency for Lebanon RTGS payments. |

3. To define further characteristics of the payment, go to **Admin Menu**>**Payments Hub**>**Local Clearing**>**Clearing Setting**.

The below screenshot displays the setup for outgoing MT103 messages.



Similar configuration can be performed for different message types (MT103 or MT202) and directions of payments (incoming and outgoing).

| Attribute | Description |
| --- | --- |
| *Message Direction* | Direction of the payment for which clearing setting record is created. |
| *Clearing Account Number* | Clearing account (Nostro) in the clearing currency. |
| *Message Payment Type* | Type of message for which the clearing setting record is created.  For example, 103 and 202. It is either 103 or 202, as TPH currently supports only these messages for Lebanon RTGS clearing. |

## Clearing Cut-off

TPH configures different cut-off times for customer (MT103) and bank transfers (MT202). To access the configuration page of cut-off, go to **Admin Menu**>**Payment Hub**>**Routing and Settlement**>**Channel Cutoff**.



In this topic

- [Configuring Lebanon RTGS](#ConfiguringLebanonRTGS)

- [Direct Participant](#DirectParticipant)
- [Clearing Cut-off](#ClearingCutoff)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:13:59 PM IST