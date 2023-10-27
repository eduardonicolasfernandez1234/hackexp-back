from django.urls import include, re_path
from rest_framework import routers

from finance.viewsets import (AccountViewSet, BalanceViewSet,
                              CategoryDocumentViewSet, CategoryFinanceViewSet,
                              DocumentDetailViewSet, DocumentViewSet,
                              ExpenseViewSet, IncomeViewSet,
                              JournalEntryLineViewSet, JournalEntryViewSet,
                              TransactionViewSet)

router = routers.DefaultRouter()
router.register(r'category-finance', CategoryFinanceViewSet)
router.register(r'category-document', CategoryDocumentViewSet)
router.register(r'account', AccountViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'document', DocumentViewSet)
router.register(r'document-detail', DocumentDetailViewSet)
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'journal-entry', JournalEntryViewSet)
router.register(r'journal-line', JournalEntryLineViewSet)
router.register(r'balance', BalanceViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
