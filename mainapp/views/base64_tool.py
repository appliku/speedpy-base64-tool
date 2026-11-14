from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class Base64ToolView(TemplateView):
    template_name = "mainapp/base64_tool.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Base64 Encoder/Decoder"
        return context

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            action = data.get('action')
            text = data.get('text', '')
            
            if not text:
                return self.render_to_json({'result': '', 'action': action, 'error': 'No input text provided'}, status=400)
            
            if action == 'encode':
                import base64
                encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
                return self.render_to_json({'result': encoded_text, 'action': 'encode'})
            elif action == 'decode':
                import base64
                try:
                    decoded_text = base64.b64decode(text.encode('utf-8')).decode('utf-8')
                    return self.render_to_json({'result': decoded_text, 'action': 'decode'})
                except Exception as e:
                    return self.render_to_json({'error': f'Decoding failed: {str(e)}'}, status=400)
            else:
                return self.render_to_json({'error': 'Invalid action. Use "encode" or "decode"'}, status=400)
        except json.JSONDecodeError:
            return self.render_to_json({'error': 'Invalid JSON in request body'}, status=400)
        except Exception as e:
            return self.render_to_json({'error': str(e)}, status=500)

    def render_to_json(self, data, status=200):
        from django.http import JsonResponse
        return JsonResponse(data, status=status)