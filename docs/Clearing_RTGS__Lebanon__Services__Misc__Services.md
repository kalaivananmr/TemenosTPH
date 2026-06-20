# Temenos Payment Services

> Source: https://docs.temenos.com/docs/Solutions/Payments/Clearing_RTGS/Lebanon/Services/Misc/Services.htm

---

2. [Payments](../../../../content/payments.html)

- Lebanon;)

Payments

# Temenos Payment Services

Updated On 22 March 2025 |
 5 Min(s) read

Feedback
Summarize

## Temenos Payments Hub (PH)

| S.No | Job Name | Description of Job | Batch Name | Classification |
| --- | --- | --- | --- | --- |
| 1 | ACCUMULATOR.RESETSERVICE | Reset RiskFilter Accumulator | PP.START.OF.DAY | FIN |
| 2 | ARC.CLUSTER.STATIC | Archival of ClusterStaticTables | ARC.CLUSTER.STATIC | FIN |
| 3 | ARC.GLOBAL.STATIC | Archival of Global Static tables | ARC.GLOBAL.STATIC | FIN |
| 4 | ARC.PORTRANSACTION | Archival of Transaction Tables | ARC.PORTRANSACTION | FIN |
| 5 | AUTRPR.TIMEOUT.SERVICE | Generating response for timed out request | AUTRPR.TIMEOUT.SERVICE | FIN |
| 6 | BAL.CHK.LISTENER.SERVICE | Service to update balance check response in asynchronus mode | BAL.CHK.LISTENER.SERVICE | FIN |
| 7 | BATCHMESSAGEMAPPINGSERVICE | Mapping Salary batch messages | BATCHMESSAGEMAPPINGSERVICE | FIN |
| 8 | BILLING.SERVICE | Generate details for external billing engine | BILLING.SERVICE | FIN |
| 9 | CHECK.FILTER.STATUS.SERVICE | Time out service Filering request | CHECK.FILTER.STATUS.SERVICE | FIN |
| 10 | CLAIMS.SERVICE | Processing pending claims | PP.END.OF.DAY1 | FIN |
| 11 | CLEARING.CRITERIA.CLEANUP | Clean up bulking criteria of clearing settlelemt service | PP.END.OF.DAY2 | FIN |
| 12 | CLEARING.SETTLEMENT.SERVICE | Service to gtoup the outgoing clearing file anf generate settlelemt transaction | CLEARING.SETTLEMENT.SERVICE | FIN |
| 13 | CUST.STATUS.RPT.GEN.MSG | Generation of Customer Status Report | PP.END.OF.DAY2 | FIN |
| 14 | CUST.STATUS.RPT.GEN.MSG.CLEANUP | CSR for Data clean up | PP.START.OF.DAY | FIN |
| 15 | INSIGHT.SERVICE | Online Service to export Payment and related static data | INSIGHT.SERVICE | FIN |
| 16 | INTERPRET.SWIFT.MESSAGE | Service to interpret and upfate Swfit Acknowlwdement message | INTERPRET.SWIFT.MESSAGE | INT |
| 17 | INWARD.MAPPING | Inward Message mapping framework Service | INWARD.MAPPING | FIN |
| 18 | INWARD.MAPPING.CLEANUP | Service  to clean record from Batch File Store records which are in REJECTED statuses | FIN |  |
| 19 | MESSAGE.ACCEPTANCE.SERVICE | Message acceptance service for single payments for specif type | MESSAGE.ACCEPTANCE.SERVICE | INT |
| 20 | MOVE.RECEIVEDFILEDTLS.TO.HIST | Mvoing the completed Received file details of the day to Hist file | PP.END.OF.DAY1 | FIN |
| 21 | OUTWARD.BULKING.SERVICE | Outward file generation via Non ESB | OUTWARD.BULKING.SERVICE | FIN |
| 22 | PAYMENT.RATE.FIXING.PROCESS | Service to calcuate the exchange rate for the payement waiting for rate fixing | PAYMENT.RATE.FIXING.PROCESS | FIN |
| 23 | PAYMENT.SOD.CLEAR.CHEQUES | Processing of Auto Clear Cheques | PAYMENT.STPFLOW.MEDIUM | FIN |
| 24 | PAYMENT.STPFLOW.HEAVY | Heavy weight payment processing STP Flow | PAYMENT.STPFLOW.HEAVY | FIN |
| 25 | PAYMENT.STPFLOW.LIGHT | Light weight payment processing STP Flow | PAYMENT.STPFLOW.LIGHT | FIN |
| 26 | PAYMENT.STPFLOW.MEDIUM | Heavy weight payment processing STP Flow | PAYMENT.STPFLOW.MEDIUM | FIN |
| 27 | PAYMENT.UNAUTH.STATUS.CHANGE | Processing of unauthorised Order Entry and Repair payments | PP.END.OF.DAY1 | FIN |
| 28 | PP.AUTO.INVSTMSG.GEN.SERVICE | Service to geneare auto investiation message to clearing | PP.AUTO.INVSTMSG.GEN.SERVICE | FIN |
| 29 | PP.CONV.STATIC.OVERRIDE | Conversion service to aling the Override on the static table | PP.CONV.STATIC.OVERRIDE | INT |
| 30 | PP.CUTOFFTIME.MONITOR | Service to provice pending payments crossed the cut off time | PP.VIRTUAL.QUEUE | INT |
| 31 | PP.EXPIRE.OUTWARD.CANCEL.REQ | Job to move the pending cancellation requests to Overdue | PP.EXPIRE.OUTWARD.CANCEL.REQ | FIN |
| 32 | PP.GENERATE.GPI.CONFIRMATIONS | Job to create Swift GPI Confirm | PP.END.OF.DAY.2 | FIN |
| 33 | PP.INTERFACE.UPDATE | Service to send out payment swfit messages | PP.INTERFACE.UPDATE | INT |
| 34 | PP.SEND.ROI.INWARD.CAN.REQ | Job to send Resolution of Investigation(camt.029) to clearing for pending cancellation request received | PP.SEND.ROI.INWARD.CAN.REQ | FIN |
| 35 | PP.UPDATE.CLIENT.CONCAT | Conversion service to update the concat file for static table | PP.UPDATE.CLIENT.CONCAT | INT |
| 36 | PP.VIRTUAL.QUEUE | Service to suppor payment enquiry | PP.VIRTUAL.QUEUE | INT |
| 37 | PPADEB.ORDER.EXPIRY | Handing of Debin Order entry payments | PPADEB.ORDER.EXPIRY | fin |
| 38 | STANDALONE.REQUEST.TIMEOUT | Service to geneare time out response for the pending standalone request | STANDALONE.REQUEST.TIMEOUT | INT |
| 39 | TPS.CONVERT.PARAMETER | Conversion of static table from PPT format to standard format | TPS.CONVERT.PARAMETER | INT |
| 40 | TPS.POR.TABLES.CONVERSION | Convertion to merge POT transaction table | TPS.POR.TABLES.CONVERSION | INT |
| 41 | WAREHOUSE.RELEASE.PAYMENTS | Releasing Warehousedpayment | PP.START.OF.DAY | FIN |
| 42 | parentFeesDetermination | Parent Transaction Fee determinaton and releasing service | parentFeesDetermination | FIN |
| 43 | DW.EXPORT.CLEAR | Exporting the payments and related parameter files for the day | PP.END.OF.DAY1 | FIN |
| 44 | DW.EXPORT.INFO | Clean up process for the DW export service | PP.END.OF.DAY1 | FIN |

## Payment Initiation (PI)

| S.No | Job Name | Description | Batch Name | Classification |
| --- | --- | --- | --- | --- |
| 1 | PAYMENT.ORDER.ARCHIVE | Job to archive the expired payment orders Hist file | PI.PURGE.PAYMENT.ORDER | FIN |
| 2 | PAYMENT.ORDER.MOVE.TO.HIS | Job to archive the completed payment orderto Hist file | PI.PURGE.PAYMENT.ORDER | FIN |
| 3 | PAYMENT.ORDER.TIMEOUT | Service to generate timeout response for Fraud check response | PAYMENT.ORDER.TIMEOUT | FIN |
| 4 | PO.PROCESS.PENDING.ORDER | Job to process warehused payment order | PI.START.OF.DAY | FIN |

## Clearing Directory(CA)

| S.No | Job Name | Description | Batch Name | Classification |
| --- | --- | --- | --- | --- |
| 1 | CLEARING.DIRECTORY.MOVE.TO.HIS | Job to move the expired / previously uploaded clearing directory records to history | CLEARING.DIRECTORY.MOVE.TO.HIS | FIN |
| 2 | POST.UPLOAD.PURGE | Service to move the expired / previously uploaded clearing directory records to history | POST.UPLOAD.PURGE |  |

In this topic

- [Temenos Payment Services](#TemenosPaymentServices)

- [Temenos Payments Hub (PH)](#TemenosPaymentsHubPH)
- [Payment Initiation (PI)](#PaymentInitiationPI)
- [Clearing Directory(CA)](#ClearingDirectoryCA)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 5:14:08 PM IST